# Activity 9 — Build a Mini Chatbot

## 1. Objective

The objective of this activity is to build a simple chatbot using an LLM through an API provider. The chatbot maintains conversation history so that it can respond based on previous messages.

## 2. Python Program

The following program uses the Groq API and stores conversation history in a list.

```python
from groq import Groq

client = Groq()

messages = [
    {
        "role": "system",
        "content": "You are a helpful chatbot. Answer clearly and simply."
    }
]

print("Mini Chatbot Started!")
print("Type 'exit' to stop the conversation.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=300
    )

    bot_reply = response.choices[0].message.content

    print("Chatbot:", bot_reply)

    messages.append({
        "role": "assistant",
        "content": bot_reply
    })
```

### How to run the program

1. Install the Groq Python library using `pip install groq`.
2. Set the `GROQ_API_KEY` environment variable with your API key.
3. Save the program as `mini_chatbot.py`.
4. Run it using `python mini_chatbot.py`.
5. Enter messages and observe how the chatbot uses earlier messages to answer follow-up questions.
6. Type `exit` to end the conversation.

## 3. Observations

### A. Why does the chatbot need to remember previous messages?

The chatbot needs conversation history to understand the context of the discussion. Previous messages help it interpret follow-up questions, remember information provided earlier in the conversation, and give relevant answers.

For example:

User: My name is Rahul.

Chatbot: Nice to meet you, Rahul!

User: What is my name?

Chatbot: Your name is Rahul.

The chatbot can answer correctly because the earlier messages are included in the request.

### B. What happens if you drop the conversation history?

If the conversation history is removed, the chatbot receives only the current message and any instructions that are still included in the request. It may not understand references to earlier messages or remember details shared previously.

For example, if the user asks, "What is my name?" without providing the earlier message containing the name, the chatbot may say that it does not know.

### C. What is the difference between this and a single one-off prompt?

A single one-off prompt sends an individual request to the model without maintaining previous conversational messages.

A chatbot with conversation history sends the relevant previous messages along with the current request. This allows it to maintain context and support natural follow-up questions.

The chatbot does not automatically remember past conversations forever. In this program, the history is stored in the Python list while the program is running. The history is lost when the program ends unless it is saved separately.

## 4. Conclusion

A mini chatbot can be built by sending user messages to an LLM and storing both user messages and assistant responses in a conversation history list. This history helps the chatbot understand context and answer follow-up questions.

Without conversation history, each request is largely independent. Therefore, maintaining history is an important feature for creating interactive conversational applications.

## 5. Result

A basic chatbot was developed using the Groq API. It accepts user input, generates responses, maintains conversation history, and continues the conversation until the user types `exit`.