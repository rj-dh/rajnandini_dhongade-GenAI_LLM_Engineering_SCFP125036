
import os
from typing import List
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.environ["API_KEY"]
)

class InterviewAnswer(BaseModel):
    question: str = Field(description="Interview question")
    answer: str = Field(description="Candidate's answer")

class ExtractedAnswers(BaseModel):
    answers: List[InterviewAnswer] = Field(description="List of interview questions and answers")

class SkillEvaluation(BaseModel):
    skill: str = Field(description="Skill being evaluated")
    demonstrated: bool = Field(description="Whether the skill is clearly demonstrated")
    evidence_or_gap: str = Field(description="Evidence from the answer or explanation of missing evidence")

class SkillEvaluations(BaseModel):
    evaluations: List[SkillEvaluation] = Field(description="Evaluation of each skill")

class ScorecardRow(BaseModel):
    skill: str = Field(description="Skill assessed")
    demonstrated: bool = Field(description="Whether the skill was demonstrated")
    evidence_or_gap: str = Field(description="Supporting evidence or identified gap")

class HiringScorecard(BaseModel):
    scorecard_rows: List[ScorecardRow] = Field(description="Final hiring scorecard rows")
    overall_recommendation: str = Field(description="Overall hiring recommendation with a brief reason")

extract_parser = PydanticOutputParser(pydantic_object=ExtractedAnswers)

evaluate_parser = PydanticOutputParser(pydantic_object=SkillEvaluations)

scorecard_parser = PydanticOutputParser(pydantic_object=HiringScorecard)

transcript_text = input("Enter interview transcript: ")
skills_input = input("Enter skills to assess, separated by commas: ")
skills_to_assess = [skill.strip() for skill in skills_input.split(",") if skill.strip()]

prompt1 = PromptTemplate(
    template="""
Extract each interview question and the candidate's corresponding answer
from the transcript. Do not invent missing answers.

{format_instructions}

Interview Transcript:
{transcript_text}
""",
    input_variables=["transcript_text"],
    partial_variables={
        "format_instructions": extract_parser.get_format_instructions()
    }
)

chain1 = prompt1 | llm | extract_parser

extracted_answers = chain1.invoke({
    "transcript_text": transcript_text
})

print("\nExtracted Interview Answers:")
print(extracted_answers)

prompt2 = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a technical interviewer evaluating skill evidence. "
        "Evaluate each requested skill using only the extracted answers. "
        "Mark a skill as demonstrated only when clear evidence supports it. "
        "Otherwise set demonstrated to false and explain the gap. "
        "Do not assume a skill from unrelated answers."
    ),
    (
        "human",
        """
Skills to Assess:
{skills_to_assess}

Extracted Answers:
{extracted_answers}

{format_instructions}
"""
    )
])

chain2 = prompt2 | llm | evaluate_parser

skill_evaluation = chain2.invoke({
    "skills_to_assess": ", ".join(skills_to_assess),
    "extracted_answers": extracted_answers.model_dump_json(),
    "format_instructions": evaluate_parser.get_format_instructions()
})

print("\nSkill Evaluation:")
print(skill_evaluation)

prompt3 = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a hiring panel coordinator. Prepare a clear, structured "
        "hiring scorecard from the supplied skill evaluations. Preserve "
        "the evidence and gaps. Base the overall recommendation on the "
        "available evidence, and do not invent candidate qualifications."
    ),
    (
        "human",
        """
Skill Evaluation:
{skill_evaluation}

{format_instructions}
"""
    )
])

chain3 = prompt3 | llm | scorecard_parser

scorecard = chain3.invoke({
    "skill_evaluation": skill_evaluation.model_dump_json(),
    "format_instructions": scorecard_parser.get_format_instructions()
})

print("\nFinal Hiring Scorecard:")
print(scorecard)
