
import os
import json
import requests
from datetime import date
from pydantic import BaseModel, Field
from urllib.parse import quote_plus
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.environ["API_KEY"]
)

class EventDetails(BaseModel):
    event_type: str = Field(description="Type of event")
    event_date: str = Field(description="Event date in YYYY-MM-DD format")
    location: str = Field(description="Event location")
    indoor_outdoor_preference: str = Field(description="Indoor, outdoor, or flexible")

class WeatherData(BaseModel):
    temperature: float = Field(description="Maximum temperature in Celsius")
    precipitation_chance: int = Field(description="Maximum precipitation probability in percent")
    conditions: str = Field(description="Weather conditions")

event_parser = PydanticOutputParser(pydantic_object=EventDetails)
weather_parser = PydanticOutputParser(pydantic_object=WeatherData)

event_prompt = PromptTemplate(
    template="""
Extract the event details from the description.
Convert the date to YYYY-MM-DD format.
If a detail is missing, use "Not specified".
Do not invent details.

{format_instructions}

Event Description:
{event_description_text}
""",
    input_variables=["event_description_text"],
    partial_variables={
        "format_instructions": event_parser.get_format_instructions()
    }
)

event_chain = event_prompt | llm | event_parser

geocoding_prompt = PromptTemplate(
    template="https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1&language=en&format=json",
    input_variables=["location"]
)

weather_prompt = PromptTemplate(
    template="https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,precipitation_probability_max,weather_code&start_date={event_date}&end_date={event_date}&timezone=auto",
    input_variables=["latitude", "longitude", "event_date"]
)

def get_weather(event):
    if event.location == "Not specified":
        raise ValueError("The event location was not specified.")

    try:
        event_day = date.fromisoformat(event.event_date)
    except ValueError:
        raise ValueError("Please provide a valid event date in YYYY-MM-DD format.")

    if event_day < date.today() or (event_day - date.today()).days > 16:
        raise ValueError("Weather forecast is available only for today through the next 16 days. Please use a date within this range.")

    geocoding_url = geocoding_prompt.format(
        location=quote_plus(event.location)
    )
    location_response = requests.get(geocoding_url, timeout=20)
    location_response.raise_for_status()
    location_data = location_response.json()

    if not location_data.get("results"):
        raise ValueError("Could not find the event location.")

    place = location_data["results"][0]

    weather_url = weather_prompt.format(
        latitude=place["latitude"],
        longitude=place["longitude"],
        event_date=event.event_date
    )

    weather_response = requests.get(weather_url, timeout=20)
    weather_response.raise_for_status()
    raw_weather = weather_response.json()

    daily = raw_weather.get("daily", {})

    if not daily.get("time") or event.event_date not in daily["time"]:
        raise ValueError("Weather data is not available for this date.")

    index = daily["time"].index(event.event_date)
    temperature = daily["temperature_2m_max"][index]
    precipitation = daily["precipitation_probability_max"][index]
    weather_code = daily["weather_code"][index]

    if temperature is None or precipitation is None or weather_code is None:
        raise ValueError("The weather API returned incomplete weather data.")

    conditions_map = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snowfall",
        73: "Moderate snowfall",
        75: "Heavy snowfall",
        80: "Rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with heavy hail"
    }

    normalized_weather = {
        "temperature": temperature,
        "precipitation_chance": precipitation,
        "conditions": conditions_map.get(weather_code, "Other weather conditions")
    }

    return weather_parser.parse(json.dumps(normalized_weather))

recommendation_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an event planning assistant. Recommend whether to proceed "
        "as planned, reschedule, or move indoors based on the event details "
        "and actual weather data. Consider the event type and indoor/outdoor "
        "preference. Explain the reason briefly. Never invent weather data. "
        "If the weather information is incomplete or uncertain, state that "
        "the organizer should verify the forecast before deciding."
    ),
    (
        "human",
        """
Event Details:
{event_details}

Weather Data:
{weather_data}

Write a practical recommendation message for the event organizer.
"""
    )
])

recommendation_chain = recommendation_prompt | llm | StrOutputParser()

event_description_text = input("Enter event description: ")

try:
    event_details = event_chain.invoke({
        "event_description_text": event_description_text
    })

    print("\nStep 1 - Structured Event Details:")
    print(event_details.model_dump_json(indent=2))

    weather_data = get_weather(event_details)

    print("\nStep 2 - Structured Weather Data:")
    print(weather_data.model_dump_json(indent=2))

    recommendation = recommendation_chain.invoke({
        "event_details": event_details.model_dump_json(),
        "weather_data": weather_data.model_dump_json()
    })

    print("\nStep 3 - Event Recommendation:")
    print(recommendation)

except (ValueError, requests.RequestException) as error:
    print("\nUnable to complete the pipeline:", error)
