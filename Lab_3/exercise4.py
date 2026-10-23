
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

#create the model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.environ["API_KEY"]
)

#take input from the user
customer_message = input("Enter customer message: ")
company_name = input("Enter company name: ")
max_words = int(input("Enter maximum words for reply: "))

#create the prompt
prompt = f"""
You are a customer support assistant for {company_name}.

Write a reply to the customer's message given below.

Customer message: {customer_message}

Instructions:
- Use a polite, friendly, and professional tone.
- Keep the same tone for every customer.
- Keep the reply within {max_words} words.
- Understand the customer's problem and respond appropriately.
- Do not make promises that are not mentioned in the message.
- Return only the customer support reply.
"""

#get the response from the model
response = llm.invoke([HumanMessage(content=prompt)])

#display the reply
print("\nCustomer Support Reply:")
print(response.content)
