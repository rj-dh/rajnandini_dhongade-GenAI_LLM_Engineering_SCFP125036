
import os
from groq import Groq

#create Groq client
client = Groq(api_key=os.environ["API_KEY"])

#classify customer review
def classify_review(review_text):

    prompt = f"""
You are a customer review classifier.

Read the customer review and classify it into one category.

Categories:
- Positive: The customer is happy with the product or service.
- Negative: The customer is unhappy with the product or service.
- Neutral: The review gives information without a clear opinion.

Rules:
- Return only one category name.
- Do not give any explanation.
- Choose only Positive, Negative, or Neutral.

Customer Review: {review_text}

Category:
"""

    response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


#take review from user
review_text = input("Enter a customer review: ")

#get and display category
category = classify_review(review_text)

print("Review Category:", category)
