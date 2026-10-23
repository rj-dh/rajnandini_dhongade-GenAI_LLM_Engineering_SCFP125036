# Activity 5 — Run an LLM Locally Using Ollama

## 1. Objective

The objective of this activity is to install Ollama, download a small language model, and run it locally to understand how local LLM inference works.

## 2. Procedure

1. Visit https://ollama.com/ and install Ollama for Linux.
2. Open the terminal and download a small model using:

   `ollama pull qwen2.5:0.5b`

3. Run the model using:

   `ollama run qwen2.5:0.5b`

4. Enter a question or prompt and observe the generated response.
5. Type `/bye` to exit the model.

## 3. Observations

### A. Does the model need internet after downloading?

No. Once Ollama and the model have been downloaded and installed, the model can generally run without an internet connection. Internet access is required for downloading models, updating Ollama, and accessing online services.

### B. Where is inference actually happening?

Inference happens locally on my computer. Ollama loads the model and performs the calculations using the available CPU and, when supported and configured, GPU resources.

The generated response is produced by my computer rather than by a remote AI server.

### C. Is any data leaving my machine?

When using a downloaded model locally through Ollama, prompts and responses are processed on the local machine and do not need to be sent to an external AI server.

However, this assumes that I am not using a remote model, external API, cloud-connected application, or another service that transmits data. Other software and network activity may also communicate externally.

### D. What happens if the model is too large for my memory?

If the model requires more memory than is available, Ollama may fail to load it, run very slowly, or cause heavy memory pressure and swapping. In severe cases, the operating system may terminate the process.

Possible solutions include choosing a smaller model, using a quantized version, reducing the context length, or using a computer with more RAM or suitable GPU memory.

## 4. Conclusion

Ollama makes it possible to run language models locally without relying on a remote AI server for every prompt. After downloading a model, basic inference can work offline. Local execution also helps keep prompts on the computer, provided no external services are used. However, the model must fit within the available system resources for reliable performance.

## 5. Result

A language model can be downloaded and executed locally using Ollama. Its internet dependency, inference location, privacy characteristics, and memory limitations can be understood through practical testing.