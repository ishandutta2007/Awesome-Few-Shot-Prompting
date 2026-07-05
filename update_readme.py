import os

readme_path = r"C:\Users\ishan\Documents\Projects\Awesome-Few-Shot-Prompting\README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "| **The Parameter Fine-Tuning Dominance Era (Traditional Deep Learning, Pre-2020)** |": "| [**The Parameter Fine-Tuning Dominance Era (Traditional Deep Learning, Pre-2020)**](pages/parameter-fine-tuning.md) |",
    "| **The In-Context Learning Scaling Revolution (GPT-3, Brown et al., 2020)** |": "| [**The In-Context Learning Scaling Revolution (GPT-3, Brown et al., 2020)**](pages/in-context-learning.md) |",
    "| **The Dynamic & Retrieval-Augmented Selection Era (~2022–2024)** |": "| [**The Dynamic & Retrieval-Augmented Selection Era (~2022–2024)**](pages/dynamic-retrieval.md) |",
    "| **The Many-Shot & Multi-Modal Long-Context Era (~2024–Present)** |": "| [**The Many-Shot & Multi-Modal Long-Context Era (~2024–Present)**](pages/many-shot.md) |",
    "| **A. Standard Input-Output Few-Shot Prompting** |": "| [**A. Standard Input-Output Few-Shot Prompting**](pages/standard-input-output.md) |",
    "| **B. Few-Shot Chain-of-Thought (CoT Prompting)** |": "| [**B. Few-Shot Chain-of-Thought (CoT Prompting)**](pages/chain-of-thought.md) |",
    "| **C. Exemplar Order Permutation Scaling** |": "| [**C. Exemplar Order Permutation Scaling**](pages/exemplar-order.md) |",
    "| **D. Interleaved Cross-Modal Few-Shot Prompting** |": "| [**D. Interleaved Cross-Modal Few-Shot Prompting**](pages/interleaved-cross-modal.md) |",
    "| **PagedAttention Prefix Cache Locking** |": "| [**PagedAttention Prefix Cache Locking**](pages/paged-attention.md) |",
    "| **Rotary Spatial Scaling Transformations (RoPE Adjustments)** |": "| [**Rotary Spatial Scaling Transformations (RoPE Adjustments)**](pages/rope-adjustments.md) |",
    "| **The KV Cache Memory Inflation and Latency Wall** |": "| [**The KV Cache Memory Inflation and Latency Wall**](pages/kv-cache.md) |",
    "| **The Data Contamination and Superficial Saturation Trap** |": "| [**The Data Contamination and Superficial Saturation Trap**](pages/data-contamination.md) |",
    "| **Enterprise Retrieval-Augmented Generation (RAG Ingestion Frameworks)** |": "| [**Enterprise Retrieval-Augmented Generation (RAG Ingestion Frameworks)**](pages/rag.md) |",
    "| **Automated Corporate Document & Multi-Axis Chart Auditing** |": "| [**Automated Corporate Document & Multi-Axis Chart Auditing**](pages/document-auditing.md) |",
    "| **Zero-Shot Synthetic Data Curation Loops (Self-Instruct)** |": "| [**Zero-Shot Synthetic Data Curation Loops (Self-Instruct)**](pages/self-instruct.md) |",
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("README updated")
