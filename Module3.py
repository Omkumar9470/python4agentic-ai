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

'''


'''

# Paragraph based chunking
new_para = """ 


Maya loved exploring the old garden behind her grandmother's house.
One afternoon, she discovered a tiny, dusty seed hidden inside a cracked clay pot. 
Her grandmother smiled and said, "That seed has been waiting for someone who believes it can grow."

Curious, Maya planted the seed in a small patch of soil and watered it every day. 
Weeks passed, but nothing happened. 
Many people told her to give up, yet she continued to care for it with patience and hope.

One morning, Maya noticed a small green sprout pushing through the earth. 
As the days went by, it grew into a beautiful tree with bright golden flowers that filled the garden with a sweet fragrance.
Neighbors came from far away just to admire its beauty.

The tree became a symbol of hope in the village. 
Whenever someone felt discouraged, they would visit the garden and remember Maya's patience and determination. 
They realized that great things often take time to grow.

From that day on, Maya understood that success is much like planting a seed. 
With faith, hard work, and patience, even the smallest dream can blossom into something extraordinary.

"""

def paragraph_chunks(text: str, min_length: int = 50) -> list[str]:
    
    paragraphs = text.split("\n\n")

    chunks = []
    for para in paragraphs:
        cleaned = para.strip()
        if len(cleaned) >= min_length:
            chunks.append(cleaned)

    return chunks


chunks = paragraph_chunks(new_para, min_length=50)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} ({len(chunk)} chars):")
    print(chunk)
    print("─" * 40)
'''


# Recursive Chunking

def recursive_chunks(
    text: str,
    chunk_size: int = 300,
    overlap: int = 30,
    separators: list[str] = None
) -> list[str]:
    
    if separators is None:
        separators = ["\n\n", "\n", ". ", " ", ""]

    def split_text(text: str, separators: list[str]) -> list[str]:

        if len(text) <= chunk_size:
            return [text.strip()] if text.strip() else []

        for sep in separators:
            if sep in text:
                parts  = text.split(sep)
                chunks = []
                current = ""

                for part in parts:
                    test = (current + sep + part).strip() if current else part.strip()

                    if len(test) <= chunk_size:
                        current = test
                    else:
                        if current:
                            chunks.append(current)

                        if len(part) > chunk_size:
                            remaining_seps = separators[separators.index(sep)+1:]
                            chunks.extend(split_text(part, remaining_seps))
                            current = ""
                        else:
                            overlap_text = current[-overlap:] if overlap and current else ""
                            current = (overlap_text + " " + part).strip() if overlap_text else part.strip()

                if current:
                    chunks.append(current)

                return [c for c in chunks if c.strip()]


        return [text[i:i+chunk_size].strip() for i in range(0, len(text), chunk_size - overlap)]

    return split_text(text, separators)

'''
chunks = recursive_chunks(SAMPLE_TEXT, chunk_size=300, overlap=30)

print(f"Total chunks: {len(chunks)}\n")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} ({len(chunk)} chars):")
    print(chunk)
    print("─" * 40)

'''

'''

# Compare strategies
import re

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

def paragraph_chunks(text: str, min_length: int = 50) -> list[str]:
    
    paragraphs = text.split("\n\n")

    chunks = []
    for para in paragraphs:
        cleaned = para.strip()
        if len(cleaned) >= min_length:
            chunks.append(cleaned)

    return chunks

def recursive_chunks(
    text: str,
    chunk_size: int = 300,
    overlap: int = 30,
    separators: list[str] = None
) -> list[str]:
    
    if separators is None:
        separators = ["\n\n", "\n", ". ", " ", ""]

    def split_text(text: str, separators: list[str]) -> list[str]:

        if len(text) <= chunk_size:
            return [text.strip()] if text.strip() else []

        for sep in separators:
            if sep in text:
                parts  = text.split(sep)
                chunks = []
                current = ""

                for part in parts:
                    test = (current + sep + part).strip() if current else part.strip()

                    if len(test) <= chunk_size:
                        current = test
                    else:
                        if current:
                            chunks.append(current)

                        if len(part) > chunk_size:
                            remaining_seps = separators[separators.index(sep)+1:]
                            chunks.extend(split_text(part, remaining_seps))
                            current = ""
                        else:
                            overlap_text = current[-overlap:] if overlap and current else ""
                            current = (overlap_text + " " + part).strip() if overlap_text else part.strip()

                if current:
                    chunks.append(current)

                return [c for c in chunks if c.strip()]


        return [text[i:i+chunk_size].strip() for i in range(0, len(text), chunk_size - overlap)]

    return split_text(text, separators)

def run_strategy(text: str, strategy: str) -> list[str]:

    strategy = strategy.lower()

    if strategy == "fixed_size_chunks":
        return fixed_size_chunks(text, chunk_size=400, overlap=50)

    elif strategy == "sentence_chunks":
        return sentence_chunks(text, sentences_per_chunk=4, overlap=2)

    elif strategy == "paragraph_chunks":
        return paragraph_chunks(text, min_length=50)

    elif strategy == "recursive_chunks":
        return recursive_chunks(text, chunk_size=300, overlap=30)

    else:
        raise ValueError(f"Unknown strategy: {strategy}")


def compare_strategies(text: str, strat1: str, strat2: str) -> list[dict]:

    chunks1 = run_strategy(text, strat1)
    chunks2 = run_strategy(text, strat2)

    print(f"\n{'='*50}")
    print(f"Strategy: {strat1}")
    print(f"{'='*50}")

    for i, chunk in enumerate(chunks1):
        print(f"Chunk {i+1} ({len(chunk)} chars):")
        print(chunk)
        print("─" * 40)

    print(f"\n{'='*50}")
    print(f"Strategy: {strat2}")
    print(f"{'='*50}")

    for i, chunk in enumerate(chunks2):
        print(f"Chunk {i+1} ({len(chunk)} chars):")
        print(chunk)
        print("─" * 40)

    comparison = [
        {
            "strategy": strat1,
            "total_chunks": len(chunks1),
            "chunks": chunks1
        },
        {
            "strategy": strat2,
            "total_chunks": len(chunks2),
            "chunks": chunks2
        }
    ]

    return comparison

compare = compare_strategies(
    SAMPLE_TEXT,
    "paragraph_chunks",
    "recursive_chunks"
)

print("\nComparison Summary")
print("=" * 50)

for item in compare:
    print(f"Strategy      : {item['strategy']}")
    print(f"Total Chunks  : {item['total_chunks']}")
    print("-" * 50)
'''

# Chunk With MetaData

def chunks_with_metadata(
    text: str,
    source: str,
    chunk_size: int = 300,
    overlap: int = 30
) -> list[dict]:
    
    raw_chunks = recursive_chunks(text, chunk_size, overlap)

    result = []
    
    for i, chunk in enumerate(raw_chunks):
        result.append({
            "id":       f"{source}_chunk_{i}",
            "text":     chunk,
            "metadata": {
                "source":       source,
                "chunk_index":  i,
                "total_chunks": len(raw_chunks),
                "char_count":   len(chunk),
                "token_approx": len(chunk) // 4,
                "word_count" : len(chunk.split()),
                "has_question" : "?" in chunk,
                "chunk_position": (
                                    "start"
                                    if i == 0
                                    else "end"
                                    if i == len(raw_chunks) - 1
                                    else "middle"
                                )
            }
        })

    return result



chunks = chunks_with_metadata(SAMPLE_TEXT, source="ai_overview.txt")

for chunk in chunks:
    print(f"ID:     {chunk['id']}")
    print(f"Text:   {chunk['text'][:60]}...")
    print(f"Meta:   {chunk['metadata']}")
    print("─" * 40)