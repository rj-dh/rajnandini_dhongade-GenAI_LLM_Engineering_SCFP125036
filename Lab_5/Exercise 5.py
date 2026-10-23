
import os
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.environ["API_KEY"]
)

class SupportSummary(BaseModel):
    issue: str = Field(description="Main issue, including any error code mentioned")
    customer_tone: str = Field(description="Customer's tone or emotion based on their words")
    resolution_attempted: str = Field(description="All troubleshooting steps already attempted")

class EscalationReadiness(BaseModel):
    missing_fields: list[str] = Field(description="Information needed for escalation that is not present in the chat")
    is_ready_to_escalate: bool = Field(description="Whether enough information is available to escalate")

summary_parser = PydanticOutputParser(pydantic_object=SupportSummary)
readiness_parser = PydanticOutputParser(pydantic_object=EscalationReadiness)

prompt1 = PromptTemplate(
    template="""
Read the complete customer support chat log carefully.

Extract the main issue, the customer's tone, and all troubleshooting
steps attempted by the customer or support.

Include error codes in the issue when they are mentioned.
Include emotions such as frustration when the customer's words show them.
Include actions such as password resets when they are mentioned.
Do not mark information as missing if it appears in the chat.
Do not invent information.

{format_instructions}

Chat Log:
{chat_log_text}
""",
    input_variables=["chat_log_text"],
    partial_variables={
        "format_instructions": summary_parser.get_format_instructions()
    }
)

chain1 = prompt1 | llm | summary_parser

prompt2 = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an escalation-readiness reviewer. Review the support "
        "summary and identify information needed for escalation that is "
        "actually missing. Check for account ID, error code when relevant, "
        "issue details, and resolution attempts. An error code included in "
        "the issue is already provided. Resolution attempts included in "
        "the summary are already provided. Do not flag information as "
        "missing if it is present. Set is_ready_to_escalate to true when "
        "enough information is available for the support team to investigate. "
        "An unavailable account ID may be flagged as missing, but it does "
        "not automatically prevent escalation if the issue can be investigated."
    ),
    (
        "human",
        """
Support Summary:
{support_summary}

{format_instructions}
"""
    )
])

chain2 = prompt2 | llm | readiness_parser

prompt3 = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a support operations lead. Create a clear and prioritized "
        "escalation report using the support summary and readiness review. "
        "Include the issue, customer tone, resolution attempts, missing "
        "information, priority, and recommended next actions. Use only "
        "provided facts. Do not invent troubleshooting results or claim "
        "that checks have already been performed. If information is missing, "
        "state what needs to be collected."
    ),
    (
        "human",
        """
Support Summary:
{support_summary}

Escalation Readiness:
{readiness_result}

Write the final escalation report for the support lead.
"""
    )
])

chain3 = prompt3 | llm | StrOutputParser()

chat_log_text = input("Enter customer support chat log: ")

support_summary = chain1.invoke({
    "chat_log_text": chat_log_text
})

print("\nStep 1 - Structured Support Summary:")
print(support_summary.model_dump_json(indent=2))

readiness_result = chain2.invoke({
    "support_summary": support_summary.model_dump_json(),
    "format_instructions": readiness_parser.get_format_instructions()
})

print("\nStep 2 - Escalation Readiness:")
print(readiness_result.model_dump_json(indent=2))

escalation_report = chain3.invoke({
    "support_summary": support_summary.model_dump_json(),
    "readiness_result": readiness_result.model_dump_json()
})

print("\nStep 3 - Escalation Report:")
print(escalation_report)
