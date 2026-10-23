
import os
from getpass import getpass
from groq import Groq


api_key = os.environ.get("API_KEY")

if not api_key:
    api_key = getpass("Enter your Groq API key: ")

client = Groq(api_key=api_key)

def generate_doctor_summary(patient_notes, patient_name):

    prompt = f"""
You are a medical documentation assistant.

Generate a clear and concise doctor's summary from the
patient consultation notes.

Patient Name: {patient_name}

Consultation Notes:
{patient_notes}

Instructions:
1. Use only the information in the notes.
2. Never invent symptoms, diagnoses, or recommendations.
3. If information is missing, write "Not provided".
4. Use professional and simple language.
5. Always follow the exact format below.

Patient Name: {patient_name}

Symptoms:
[Summarize the reported symptoms]

Diagnosis:
[State the documented diagnosis or Not provided]

Recommendation:
[Summarize documented recommendations or Not provided]
"""

    response = client.chat.completions.create(
       model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a medical documentation assistant. "
                    "Follow the requested output format exactly. "
                    "Never make up medical information."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    print("=" * 45)
    print("DOCTOR SUMMARY GENERATOR")
    print("=" * 45)

    patient_name = input("\nEnter patient name: ").strip()

    print(
        "\nEnter consultation notes below."
        "\nType END on a new line when finished:"
    )

    notes_lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        notes_lines.append(line)

    patient_notes = "\n".join(notes_lines).strip()

    if not patient_name or not patient_notes:
        print("\nError: Patient name and notes are required.")

    else:
        try:
            summary = generate_doctor_summary(
                patient_notes,
                patient_name
            )

            print("\n" + "=" * 45)
            print("GENERATED DOCTOR SUMMARY")
            print("=" * 45)
            print(summary)

        except Exception as error:
            print(f"\nError generating summary: {error}")
