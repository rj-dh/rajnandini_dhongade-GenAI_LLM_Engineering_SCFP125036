
import os
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser

# Initialize Groq LLM using API key
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.environ["API_KEY"]
)

# Step 1: Define the structure for customer review data
class ReviewData(BaseModel):
    complaint: str = Field(description="Main complaint of the customer")
    product_or_feature: str = Field(description="Product or feature mentioned")
    sentiment: str = Field(description="Customer sentiment")

parser = PydanticOutputParser(pydantic_object=ReviewData)

review_text = input("Enter customer review: ")

prompt1 = PromptTemplate(
    template="""
Extract the main complaint, product or feature, and customer sentiment
from the customer review below.

{format_instructions}

Customer Review:
{review_text}
""",
    input_variables=["review_text"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

#first chain
chain1 = prompt1 | llm | parser

#structured review data
review_data = chain1.invoke({"review_text": review_text})

print("\nExtracted Review Data:")
print(review_data)

# Step 2: Create a prompt for writing the support ticket
prompt2 = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a support ticket writer. Write a short and clear "
        "support ticket summary for the internal support team. "
        "Use only the structured data provided."
    ),
    (
        "human",
        """
Complaint: {complaint}
Product or Feature: {product_or_feature}
Sentiment: {sentiment}

Write the support ticket summary.
"""
    )
])

# Create the second chain
chain2 = prompt2 | llm | StrOutputParser()

# Pass only the structured data from Step 1
ticket = chain2.invoke({
    "complaint": review_data.complaint,
    "product_or_feature": review_data.product_or_feature,
    "sentiment": review_data.sentiment
})

print("\nSupport Ticket Summary:")
print(ticket)
