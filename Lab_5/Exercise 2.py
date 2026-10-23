
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

# Step 1: Define the structure for research paper information
class ResearchData(BaseModel):
    research_question: str = Field(description="Main research question")
    method: str = Field(description="Method used in the research")
    key_finding: str = Field(description="Main finding of the research")

# Create the output parser
parser = PydanticOutputParser(pydantic_object=ResearchData)

# Take research paper abstract as input
abstract_text = input("Enter research paper abstract: ")

# Step 1: Extract information from the abstract
prompt1 = PromptTemplate(
    template="""
Read the research paper abstract and extract the research question,
method, and key finding.

{format_instructions}

Research Paper Abstract:
{abstract_text}
""",
    input_variables=["abstract_text"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# Create the first chain
chain1 = prompt1 | llm | parser

# Get structured research data
research_data = chain1.invoke({"abstract_text": abstract_text})

print("\nExtracted Research Data:")
print(research_data)

# Step 2: Create a prompt for a plain-language summary
prompt2 = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a science communicator explaining research to a general "
        "audience. Use simple everyday language and avoid technical jargon. "
        "Use only the structured research data provided."
    ),
    (
        "human",
        """
Research Question: {research_question}
Method: {method}
Key Finding: {key_finding}

Explain this research in a short, simple paragraph for a non-expert.
"""
    )
])

# Create the second chain
chain2 = prompt2 | llm | StrOutputParser()

# Pass only the structured data from Step 1
summary = chain2.invoke({
    "research_question": research_data.research_question,
    "method": research_data.method,
    "key_finding": research_data.key_finding
})

print("\nLayperson Summary:")
print(summary)

