# The Dynamic & Retrieval-Augmented Selection Era (~2022–2024)

This era focuses on dynamically retrieving relevant examples for the prompt to improve few-shot performance.

```mermaid
graph LR
    A[User Query] --> B[Vector DB Search]
    B --> C[Top-K Examples Retrieval]
    C --> D[Prompt Assembly]
    D --> E[Model Inference]
```

[Back to README](../README.md)
