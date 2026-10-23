# Activity 4 — Can My Computer Run an LLM?

## 1. Check RAM and GPU

My laptop uses Pop!_OS Linux. Based on my previous system check, it has approximately 30 GB of RAM and an AMD Radeon RX 5500M dedicated GPU, along with integrated AMD Radeon Vega graphics.

The following commands can be used to check system specifications in the terminal:

Check RAM:
`free -h`

Check GPU:
`lspci | grep -Ei 'vga|3d|display'`

Check GPU memory and utilization:
`radeontop`

## 2. Compare Memory Requirements at Different Precisions

For a computer with 8 GB of RAM, the approximate memory requirements are:

**A. 4B FP16**

- A model with 4 billion parameters stored in FP16 requires approximately 8 GB for model weights alone.
- Additional memory is required by the operating system and the inference process.
- Therefore, it is generally not practical to run this configuration comfortably on an 8 GB RAM computer.

**B. 4B INT4**

- A model with 4 billion parameters stored in 4-bit precision requires approximately 2 GB for model weights.
- Additional memory is required for the inference process and other operations.
- This is a practical choice for an 8 GB RAM computer because it leaves more memory available for other tasks.

**C. 7B INT4**

- A model with 7 billion parameters stored in 4-bit precision requires approximately 3.5 GB for model weights.
- Additional memory is needed for the operating system, model runtime, and context.
- It may run on an 8 GB RAM computer, but memory limitations can affect performance and usability.

These are approximate weight-storage calculations. Actual memory usage varies with the model format, quantization method, runtime, and context length.

## 3. What Else Besides Model Weights Uses Memory?

Model execution requires memory for several components:

1. **Operating system:** Memory used by Linux and background applications.
2. **Model runtime:** Memory used by Python, libraries, and inference software.
3. **KV cache:** Memory used to retain information about previous tokens during text generation.
4. **Input and output tokens:** Memory required to process prompts and generate responses.
5. **Intermediate computations:** Temporary memory used while the model performs calculations.

Therefore, the total memory requirement is always greater than the memory needed for model weights alone.

## 4. Would Quantization Always Be the Safer Choice?

No. Quantization reduces model memory requirements by representing model weights with fewer bits. However, it can sometimes reduce output quality or accuracy.

The best choice depends on the available hardware and the task. A quantized model may be more practical on a computer with limited memory, while a higher-precision model may provide better numerical accuracy.

Quantization also does not eliminate the memory needed for the KV cache, intermediate computations, and other runtime operations.

## 5. Conclusion

For a computer with 8 GB of RAM, a 4B INT4 model is generally the safest option among the three because it requires less memory than a 4B FP16 or 7B INT4 model.

A 7B INT4 model may also run, but it leaves less memory available for other operations. A 4B FP16 model requires approximately 8 GB for weights alone, making it unsuitable for comfortable execution on an 8 GB RAM system.

Quantization makes local LLM execution more accessible, but the final choice must consider memory requirements, output quality, and hardware compatibility.