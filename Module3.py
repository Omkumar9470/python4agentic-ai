SAMPLE_TEXT = """
Artificial intelligence is transforming every industry.
Machine learning, a subset of AI, enables systems to learn
from data without being explicitly programmed.

Deep learning uses neural networks with many layers
to process complex patterns. It powers image recognition,
speech processing, and natural language understanding.

Large language models are a type of deep learning model
trained on massive text datasets. They can generate text,
answer questions, and solve complex reasoning tasks.

Retrieval Augmented Generation combines LLMs with external
knowledge bases. It reduces hallucination and allows models
to access private or real-time information.

Vector databases store embeddings and enable fast
similarity search. ChromaDB, Pinecone, and Weaviate
are popular vector database solutions.
"""


# Fixed Size Chunking

def fixed_size_chunks(text: str, chunk_size: int = 200, overlap: int = 20) -> list[str]:
    
    chunks = []
    start  = 0

    while start < len(text):
        end   = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


chunks = fixed_size_chunks(SAMPLE_TEXT, chunk_size=400, overlap=50)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} ({len(chunk)} chars):")
    print(chunk)
    print("─" * 40)