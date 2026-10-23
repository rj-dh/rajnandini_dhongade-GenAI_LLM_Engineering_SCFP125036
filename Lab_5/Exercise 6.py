
import os
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.environ["API_KEY"]
)

class FitnessGoal(BaseModel):
    goal_type: str = Field(description="Main fitness goal")
    fitness_level: str = Field(description="Current fitness level")
    days_available: int = Field(description="Number of days available per week")
    equipment_access: str = Field(description="Available workout equipment")

class WorkoutDay(BaseModel):
    day: str = Field(description="Day of the week")
    workout_focus: str = Field(description="Main workout focus")
    exercises: list[str] = Field(description="List of exercises")
    duration_minutes: int = Field(description="Workout duration in minutes")

class WeeklyWorkoutPlan(BaseModel):
    weekly_plan: list[WorkoutDay] = Field(description="Day-by-day weekly workout plan")

goal_parser = PydanticOutputParser(pydantic_object=FitnessGoal)
plan_parser = PydanticOutputParser(pydantic_object=WeeklyWorkoutPlan)

prompt1 = PromptTemplate(
    template="""
Extract the fitness goal details from the user's description.
Use a fitness level such as beginner, intermediate, or advanced.
The number of available days must be between 1 and 7.
If equipment or fitness level is not specified, state that it is not specified.
Do not invent personal details.

{format_instructions}

Fitness Goal Description:
{fitness_goal_text}

Days Available Per Week:
{days_per_week}
""",
    input_variables=["fitness_goal_text", "days_per_week"],
    partial_variables={
        "format_instructions": goal_parser.get_format_instructions()
    }
)

chain1 = prompt1 | llm | goal_parser

prompt2 = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a certified personal trainer. Create a practical weekly "
        "workout plan using only the extracted fitness goal details provided "
        "below. Do not use or assume any information from the original "
        "description. Create exactly the number of workout days specified. "
        "Use suitable exercises for the fitness level and available equipment. "
        "Include rest days by leaving the remaining days out of the workout "
        "list. Keep the plan realistic and include a warm-up or cool-down "
        "where appropriate. Avoid unsafe or extreme training."
    ),
    (
        "human",
        """
Extracted Fitness Goal Details:
{fitness_goal_details}

{format_instructions}
"""
    )
])

chain2 = prompt2 | llm | plan_parser

fitness_goal_text = input("Enter your fitness goal description: ")
days_per_week = input("How many days per week are you available to work out? ")

try:
    days = int(days_per_week)

    if days < 1 or days > 7:
        raise ValueError("Days per week must be between 1 and 7.")

    fitness_goal = chain1.invoke({
        "fitness_goal_text": fitness_goal_text,
        "days_per_week": days
    })

    print("\nStep 1 - Extracted Fitness Goal Details:")
    print(fitness_goal.model_dump_json(indent=2))

    workout_plan = chain2.invoke({
        "fitness_goal_details": fitness_goal.model_dump_json(),
        "format_instructions": plan_parser.get_format_instructions()
    })

    print("\nStep 2 - Weekly Workout Plan:")
    print(workout_plan.model_dump_json(indent=2))

except ValueError as error:
    print("Invalid input:", error)
