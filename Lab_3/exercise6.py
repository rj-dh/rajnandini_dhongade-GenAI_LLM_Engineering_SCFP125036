
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.environ["API_KEY"]
)

draft_text = input("Enter your draft text: ")
issue_to_fix = input("Enter the issue to fix: ")

revised_text = draft_text

for round_number in range(1, 4):
    print(f"\nRound {round_number}")

    prompt = f"""
You are a content editor.

Draft text:
{revised_text}

Issue to fix:
{issue_to_fix}

Instructions:
- Fix only the specific issue mentioned.
- Keep the original meaning.
- Do not introduce unrelated changes.
- Return only the revised text.
"""
    response = llm.invoke([HumanMessage(content=prompt)])

    revised_text = response.content.strip()

    print(revised_text)

print("\nFinal Revised Text:")
print(revised_text)

