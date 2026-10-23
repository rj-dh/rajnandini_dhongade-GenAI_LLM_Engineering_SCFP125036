
import os
import json
from groq import Groq

#create Groq client
client = Groq(api_key=os.environ["API_KEY"])


#function to extract resume details
def extract_resume_fields(resume_text, fields_to_extract):

    prompt = f"""
You are a resume field extractor.

Read the resume text and extract only the requested fields.

Resume Text:
{resume_text}

Fields to Extract:
{fields_to_extract}

Instructions:
- Return the result in valid JSON format.
- Include only the requested fields.
- Do not add any extra fields.
- If a field is not available in the resume, use null.
- Do not include explanations or text outside the JSON.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    result = response.choices[0].message.content.strip()

    #convert json text into a python dictionary
    return json.loads(result)


#get resume text from the user
resume_text = input("Enter resume text: ")

# Enter the fields to extract
fields_input = input(
    "Enter fields to extract (separated by commas): "
)

fields_to_extract = [
    field.strip() for field in fields_input.split(",")
]

#extract and display the result
try:
    extracted_data = extract_resume_fields(
        resume_text,
        fields_to_extract
    )

    print("\nExtracted Resume Details:")
    print(json.dumps(extracted_data, indent=4))

except json.JSONDecodeError:
    print("Error: The model did not return valid JSON.")

except Exception as error:
    print("Error:", error)
