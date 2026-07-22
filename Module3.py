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


'''
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

'''

# Sentence Based Chunking

import re

def sentence_chunks(text: str, sentences_per_chunk: int = 3, overlap: int = 1) -> list[str]:

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [s.strip() for s in sentences if s.strip()]

    chunks = []
    step   = sentences_per_chunk - overlap

    for i in range(0, len(sentences), step):
        chunk = " ".join(sentences[i:i + sentences_per_chunk])
        if chunk:
            chunks.append(chunk)

    return chunks



chunks = sentence_chunks(SAMPLE_TEXT, sentences_per_chunk=4, overlap=2)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:")
    print(chunk)
    print("─" * 40)