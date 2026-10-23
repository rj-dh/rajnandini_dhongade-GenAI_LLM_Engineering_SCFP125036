
# Activity 7 — Compare Local vs Colab vs API

## 1. Comparison of Local, Google Colab, and API-Based Execution

| Feature | Local Execution | Google Colab GPU | API / Inference Provider |
|---|---|---|---|
| Where inference happens | On my computer | On a cloud-hosted runtime | On the provider's servers |
| Hardware required locally | Sufficient RAM and CPU | Internet-connected computer | Internet-connected computer |
| GPU requirement | Optional for small models | GPU can be enabled when available | Managed by the provider |
| Internet requirement | Not required after setup and model download | Required | Required |
| Cost | Uses my own hardware and electricity | Free or paid plans, depending on usage | Free limits or paid usage, depending on provider |
| Privacy | High when processing stays entirely local | Data is processed in a cloud environment | Data is sent to an external provider |
| Scalability | Limited by local hardware | Depends on available cloud resources | Generally high, depending on provider limits |
| Best use | Offline work and privacy-sensitive tasks | Learning, experimentation, and GPU-based tasks | Applications requiring convenient access to powerful models |

## 2. If You Had an 8 GB RAM Laptop With No GPU, Which Approach Would You Pick?

I would choose an API or inference provider for running medium or large language models because the provider handles the computing requirements. My laptop would only need to send prompts and receive responses.

For learning and experimenting with small models, I would also consider local execution using a lightweight, quantized model. Google Colab would be another good option when I need access to a GPU for experiments.

Therefore, my choice would depend on the model size, privacy requirements, and available budget.

## 3. Which Approach Is the Most Private? Which Is the Most Scalable?

### Most private: Local execution

Local execution is generally the most private option when the model runs entirely on my computer and no prompts or outputs are sent to external services. Sensitive information can remain on my device.

### Most scalable: API / inference provider

An API is generally the easiest option to scale because the provider manages the computing infrastructure and can support many requests, subject to its capacity, rate limits, and pricing.

Google Colab is useful for experiments that need additional computing resources, but it is not usually the best choice for deploying a continuously available application.

## 4. When Would You Choose Local Over Cloud, or the Reverse?

### I would choose local execution when:

1. I need to work without an internet connection.
2. I want to keep sensitive data on my computer.
3. I want to experiment without per-request API charges.
4. The model is small enough to run comfortably on my hardware.

### I would choose Google Colab when:

1. My laptop does not have a suitable GPU.
2. I want to learn about deep learning or experiment with larger models.
3. I need temporary access to cloud computing resources.
4. I am testing code or models in a notebook environment.

### I would choose an API when:

1. I need to access a powerful model without downloading it.
2. I am developing an application that needs to generate responses.
3. I want to avoid managing model installation and hardware.
4. I need an approach that can scale with application demand.

## 5. Conclusion

Local execution provides greater control and privacy, but performance is limited by available hardware. Google Colab provides convenient access to cloud computing resources for experimentation. APIs simplify access to powerful models and make scaling applications easier, but they require internet access and may involve usage costs.

For an 8 GB RAM laptop without a GPU, I would use a small quantized model locally for basic learning and choose an API or Google Colab when more computing power is required. The final choice depends on privacy, performance, cost, and the purpose of the application.

## 6. Result

The three approaches were compared based on hardware requirements, privacy, cost, scalability, and practical use cases. Each approach has advantages, and the most suitable option depends on the user's requirements and available resources.