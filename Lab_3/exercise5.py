
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.environ["API_KEY"]
)

sentence = input("Enter a sentence: ")
target_language = input("Enter target language: ")
formality = input("Enter formality (formal or informal): ")

prompt = f"""
Translate the following sentence into {target_language}.

Sentence: {sentence}

Instructions:
- Use a {formality} tone.
- Keep the original meaning of the sentence.
- Make the translation natural and easy to understand.
- Do not add extra information.
- Return only the translated sentence.
"""

response = llm.invoke([HumanMessage(content=prompt)])

print("\nTranslated Sentence:")
print(response.content)
