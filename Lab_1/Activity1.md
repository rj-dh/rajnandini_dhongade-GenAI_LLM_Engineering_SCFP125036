# Activity 1 — Explore LLM Models on Hugging Face

## 1. Small Model: Qwen2.5-0.5B-Instruct

1. **Created by:** Qwen Team, Alibaba.
2. **Number of parameters:** 0.49 billion (approximately 500 million).
3. **Is it a generative model?** Yes. It generates text, answers questions, and follows instructions.
4. **Context length:** 32,768 tokens.
5. **Suitable for local execution?** Yes. It can run on a normal computer with sufficient RAM, even without a dedicated GPU.
6. **Recommended hardware:** A standard computer with adequate RAM. A GPU is optional for basic experimentation.

Hugging Face link: https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct

## 2. Medium Model: Qwen2.5-7B-Instruct

1. **Created by:** Qwen Team, Alibaba.
2. **Number of parameters:** 7.61 billion.
3. **Is it a generative model?** Yes. It generates text, answers questions, follows instructions, and assists with coding.
4. **Context length:** 131,072 tokens.
5. **Suitable for local execution?** Yes, if the computer has sufficient RAM or GPU memory. Quantization can reduce memory requirements.
6. **Recommended hardware:** A capable GPU with sufficient VRAM is recommended for faster performance. CPU execution is also possible with sufficient system RAM.

Hugging Face link: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

## 3. Large Model: Qwen2.5-72B-Instruct

1. **Created by:** Qwen Team, Alibaba.
2. **Number of parameters:** 72.7 billion.
3. **Is it a generative model?** Yes. It generates text, follows complex instructions, and handles advanced language tasks.
4. **Context length:** 131,072 tokens.
5. **Suitable for local execution?** Yes, but it is generally impractical to run on an ordinary laptop because of its high memory requirements.
6. **Recommended hardware:** Multiple high-memory GPUs or a powerful multi-GPU server. Quantization can reduce memory requirements but still requires substantial resources.

Hugging Face link: https://huggingface.co/Qwen/Qwen2.5-72B-Instruct

## Conclusion

The small model is suitable for beginners and local experimentation because it requires fewer computing resources. The medium model offers a balance between performance and hardware requirements. The large model can handle demanding tasks but requires significantly more memory and computing power.

Therefore, the small model is the best starting point for running an LLM on a personal computer, while the medium and large models are more suitable for systems with greater hardware capacity.

## References

1. https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct
2. https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
3. https://huggingface.co/Qwen/Qwen2.5-72B-Instruct