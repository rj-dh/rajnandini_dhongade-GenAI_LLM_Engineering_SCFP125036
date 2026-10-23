# Activity 3 — Run an LLM Using Google Colab GPU

## 1. Objective

The objective of this activity is to run a small Large Language Model (LLM) using Google Colab with a GPU runtime and observe its GPU usage, memory consumption, and text generation performance.

## 2. Procedure

1. Open Google Colab at https://colab.research.google.com/.
2. Create a new notebook.
3. Select Runtime → Change runtime type.
4. Select a GPU under Hardware accelerator and click Save.
5. Install the required libraries and load a small language model.
6. Generate text and observe GPU utilization and memory consumption.

Example model: Qwen2.5-0.5B-Instruct.

## 3. Observations

### A. Is the GPU actually being used?

When the model is loaded onto the GPU and text generation is performed, GPU memory usage and computation increase. This can be checked using the following command in a Colab code cell:

`!nvidia-smi`

If the model is running on the CPU instead, GPU memory usage may remain low. Simply enabling a GPU runtime does not guarantee that the model is using it.

### B. How much memory does the model consume?

The Qwen2.5-0.5B-Instruct model has approximately 0.49 billion parameters. Its weights require roughly 1 GB of memory when stored at 16-bit precision. Additional GPU memory is needed for intermediate computations, the attention cache, and other overhead.

Actual memory consumption depends on the model precision, software, and input and output lengths.

### C. What happens if you increase the output length?

Increasing the output length allows the model to generate more tokens. This generally increases generation time and memory consumption because the model must maintain more context during generation.

Longer outputs can also increase GPU utilization and latency. The exact effect depends on the model and hardware.

### D. Would this run on a laptop without a GPU?

Yes. A small model such as Qwen2.5-0.5B-Instruct can run on a laptop using its CPU, provided sufficient system RAM is available. However, text generation may be slower than on a suitable GPU.

Larger models generally require more memory and computing power, so a GPU or cloud-based environment can make execution more practical.

## 4. Conclusion

Google Colab provides access to GPU resources for running and experimenting with LLMs. GPU utilization can be verified using `nvidia-smi`, while memory consumption depends on the model size, precision, and sequence length. Increasing the output length generally increases generation time and can increase memory usage. Small language models can also run on laptops without dedicated GPUs, although inference may be slower.

## 5. Result

A small LLM can be executed using Google Colab with a GPU runtime. Its hardware usage and generation performance can be studied by monitoring GPU utilization, memory consumption, and output length.