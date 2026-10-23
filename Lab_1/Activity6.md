# Activity 6 — Use an LLM Through an API / Inference Provider

## 1. Objective

The objective of this activity is to understand how to access a Large Language Model (LLM) through an API or an inference provider and compare cloud-based inference with local execution.

## 2. Procedure

1. Choose an inference provider, such as Groq or Hugging Face.
2. Create an account and obtain an API key.
3. Install the required Python library.
4. Write a Python program that sends a prompt to the provider's API.
5. Receive and display the model's generated response.

Example Python code using the Groq API:

```python
from groq import Groq

client = Groq()  # Reads GROQ_API_KEY from the environment

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Explain what an LLM is."}
    ]
)

print(response.choices[0].message.content)
```

The API key should be stored securely in an environment variable named `GROQ_API_KEY`. The example model must be available to the account and provider at the time of execution.

## 3. Observations

### A. What is actually happening between the program and the model?

My Python program sends a request containing the prompt and other required information to the provider's API over the internet. The provider processes the request, runs the model on its servers, and sends the generated response back to my program.

The program displays the returned text to the user. Therefore, the model's inference happens on the provider's infrastructure rather than on my local computer.

### B. Who is paying for compute here?

The inference provider pays for the servers, GPUs, electricity, and infrastructure required to run the model.

Depending on the provider and service plan, the user may pay according to the number of tokens processed, the number of requests, or the amount of computing time used. Some providers also offer free usage limits or trial credits.

### C. What are the trade-offs versus running locally?

**Advantages of using an API:**

1. No need to download or store large model files locally.
2. Less demand on my computer's RAM and GPU.
3. Access to powerful models using a simple API.
4. Model infrastructure and maintenance are managed by the provider.

**Disadvantages of using an API:**

1. An internet connection is generally required.
2. Usage may involve costs or rate limits.
3. Prompts and other request data are sent to an external provider.
4. Performance depends on network speed and provider availability.
5. The user has less control over the model's infrastructure and configuration.

**Advantages of running locally:**

1. Prompts can remain on my computer.
2. Basic inference can work without internet after setup.
3. There are no per-request API charges for local inference.
4. I have greater control over model files and execution settings.

However, local execution requires sufficient hardware resources and uses my own computer's memory, processing power, and electricity.

## 4. Conclusion

An API allows a Python program to communicate with a remotely hosted language model. The program sends a request to the provider, the provider performs inference on its servers, and the generated response is returned to the program.

The provider manages the computing infrastructure, while the user may pay through usage-based pricing or a subscription. Compared with local execution, APIs provide easier access to powerful models and reduce local hardware requirements, but they introduce internet dependency, possible costs, and additional data-privacy considerations.

## 5. Result

The process of accessing an LLM through an API was studied. The activity demonstrates how programs communicate with remote models and explains the differences between cloud-based inference and local inference.