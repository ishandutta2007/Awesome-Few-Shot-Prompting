import os

pages_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Few-Shot-Prompting\pages"
os.makedirs(pages_dir, exist_ok=True)

pages = {
    "parameter-fine-tuning.md": {
        "title": "The Parameter Fine-Tuning Dominance Era (Traditional Deep Learning, Pre-2020)",
        "content": "This era represents the traditional approach to machine learning where model weights are updated through backpropagation.\n\n```mermaid\ngraph LR\n    A[Dataset] --> B[Training]\n    B --> C[Model Weights Update]\n    C --> D[Task Specific Model]\n```"
    },
    "in-context-learning.md": {
        "title": "The In-Context Learning Scaling Revolution (GPT-3, Brown et al., 2020)",
        "content": "In-context learning emerged with GPT-3, allowing models to learn from prompt examples without weight updates.\n\n```mermaid\ngraph LR\n    A[Prompt Examples] --> B[Transformer Context Window]\n    B --> C[In-Context Pattern Recognition]\n    C --> D[Zero-Shot/Few-Shot Output]\n```"
    },
    "dynamic-retrieval.md": {
        "title": "The Dynamic & Retrieval-Augmented Selection Era (~2022–2024)",
        "content": "This era focuses on dynamically retrieving relevant examples for the prompt to improve few-shot performance.\n\n```mermaid\ngraph LR\n    A[User Query] --> B[Vector DB Search]\n    B --> C[Top-K Examples Retrieval]\n    C --> D[Prompt Assembly]\n    D --> E[Model Inference]\n```"
    },
    "many-shot.md": {
        "title": "The Many-Shot & Multi-Modal Long-Context Era (~2024–Present)",
        "content": "Modern models support massive context windows, enabling many-shot prompting with hundreds of examples.\n\n```mermaid\ngraph TB\n    A[Massive Context Window] --> B[Many-Shot Examples]\n    A --> C[Code Repos]\n    A --> D[Images & Audio]\n    B & C & D --> E[Highly Adapted Inference]\n```"
    },
    "standard-input-output.md": {
        "title": "A. Standard Input-Output Few-Shot Prompting",
        "content": "Standard I/O prompting maps inputs directly to outputs in the prompt context.\n\n```mermaid\ngraph LR\n    A[Input 1] --> B[Output 1]\n    C[Input 2] --> D[Output 2]\n    E[Target Input] --> F[Predicted Output]\n```"
    },
    "chain-of-thought.md": {
        "title": "B. Few-Shot Chain-of-Thought (CoT Prompting)",
        "content": "CoT introduces intermediate reasoning steps before providing the final answer.\n\n```mermaid\ngraph LR\n    A[Input] --> B[Step-by-Step Reasoning]\n    B --> C[Final Output]\n```"
    },
    "exemplar-order.md": {
        "title": "C. Exemplar Order Permutation Scaling",
        "content": "Varying the order of examples helps mitigate the recency bias in LLMs.\n\n```mermaid\ngraph TB\n    A[Order 1] --> D[Ensemble/Average]\n    B[Order 2] --> D\n    C[Order 3] --> D\n    D --> E[Final Robust Output]\n```"
    },
    "interleaved-cross-modal.md": {
        "title": "D. Interleaved Cross-Modal Few-Shot Prompting",
        "content": "Combining text and images in few-shot prompts for Vision-Language Models.\n\n```mermaid\ngraph LR\n    A[Image 1 + Text 1] --> B[Context Sequence]\n    C[Image 2 + Text 2] --> B\n    B --> D[Cross-Modal Attention]\n```"
    },
    "paged-attention.md": {
        "title": "PagedAttention Prefix Cache Locking",
        "content": "PagedAttention optimizes memory management by sharing prefix caches across requests.\n\n```mermaid\ngraph TB\n    A[Shared Prefix Tokens] --> B[Paged KV Cache]\n    B --> C[User Request 1]\n    B --> D[User Request 2]\n```"
    },
    "rope-adjustments.md": {
        "title": "Rotary Spatial Scaling Transformations (RoPE Adjustments)",
        "content": "RoPE allows models to handle very long sequences effectively by encoding relative positions.\n\n```mermaid\ngraph LR\n    A[Token i] --> B[Rotary Transformation]\n    C[Token j] --> D[Rotary Transformation]\n    B & D --> E[Relative Distance Encoded]\n```"
    },
    "kv-cache.md": {
        "title": "The KV Cache Memory Inflation and Latency Wall",
        "content": "Addressing the challenges of large KV caches with techniques like Grouped-Query Attention.\n\n```mermaid\ngraph TB\n    A[Full KV Cache] --> B[GQA / Compression]\n    B --> C[Reduced VRAM Footprint]\n```"
    },
    "data-contamination.md": {
        "title": "The Data Contamination and Superficial Saturation Trap",
        "content": "Preventing models from memorizing benchmark data by using dynamic evaluation.\n\n```mermaid\ngraph LR\n    A[Static Benchmarks] -->|Contamination| B[Memorized Output]\n    C[Dynamic Live Registries] -->|Authentic Evaluation| D[True Generalization]\n```"
    },
    "rag.md": {
        "title": "Enterprise Retrieval-Augmented Generation (RAG Ingestion Frameworks)",
        "content": "Using enterprise data to ground model generations and prevent hallucinations.\n\n```mermaid\ngraph LR\n    A[Enterprise Data] --> B[Embedding Model]\n    B --> C[Vector DB]\n    D[User Query] --> C\n    C --> E[Context + Query]\n    E --> F[LLM Generation]\n```"
    },
    "document-auditing.md": {
        "title": "Automated Corporate Document & Multi-Axis Chart Auditing",
        "content": "Processing complex multi-modal documents with long-context LLMs.\n\n```mermaid\ngraph TB\n    A[PDFs] --> D[Long Context Window]\n    B[Charts] --> D\n    C[Codebooks] --> D\n    D --> E[Compliance Report]\n```"
    },
    "self-instruct.md": {
        "title": "Zero-Shot Synthetic Data Curation Loops (Self-Instruct)",
        "content": "Using strong models to generate synthetic instruction data for smaller models.\n\n```mermaid\ngraph LR\n    A[Seed Instructions] --> B[Teacher LLM Generation]\n    B --> C[Synthetic Dataset]\n    C --> D[Student Model Fine-Tuning]\n```"
    }
}

for filename, data in pages.items():
    path = os.path.join(pages_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {data['title']}\n\n")
        f.write(f"{data['content']}\n\n")
        f.write(f"[Back to README](../README.md)\n")
