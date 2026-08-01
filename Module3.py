'''SAMPLE_TEXT = """
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
'''
'''
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

'''
'''
# Universal chunker assignment

class UniversalChunker:

    def __init__(self, chunk_size=300, overlap=30):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str, source: str, strategy: str = "recursive") -> list[dict]:

        if strategy.lower() == "fixed":
            raw_chunks = fixed_size_chunks(
                text,
                chunk_size=self.chunk_size,
                overlap=self.overlap
            )

        elif strategy.lower() == "sentence":
            raw_chunks = sentence_chunks(
                text,
                sentences_per_chunk=3,
                overlap=1
            )

        elif strategy.lower() == "paragraph":
            raw_chunks = paragraph_chunks(
                text,
                min_length=50
            )

        elif strategy.lower() == "recursive":
            raw_chunks = recursive_chunks(
                text,
                chunk_size=self.chunk_size,
                overlap=self.overlap
            )

        else:
            raise ValueError(f"Unknown strategy: {strategy}")

        result = []

        for i, chunk in enumerate(raw_chunks):

            if i == 0:
                position = "start"
            elif i == len(raw_chunks) - 1:
                position = "end"
            else:
                position = "middle"

            result.append(
                {
                    "id": f"{source}_chunk_{i}",
                    "text": chunk,
                    "metadata": {
                        "source": source,
                        "chunk_index": i,
                        "total_chunks": len(raw_chunks),
                        "char_count": len(chunk),
                        "token_approx": len(chunk) // 4,
                        "word_count": len(chunk.split()),
                        "has_question": "?" in chunk,
                        "chunk_position": position
                    }
                }
            )

        return result

    def stats(self, chunks: list[dict]):

        lengths = [
            chunk["metadata"]["char_count"]
            for chunk in chunks
        ]

        tokens = sum(
            chunk["metadata"]["token_approx"]
            for chunk in chunks
        )

        print("=" * 50)
        print("Chunk Statistics")
        print("=" * 50)
        print(f"Total Chunks   : {len(chunks)}")
        print(f"Average Length : {sum(lengths) / len(lengths):.2f} chars")
        print(f"Minimum Length : {min(lengths)} chars")
        print(f"Maximum Length : {max(lengths)} chars")
        print(f"Approx Tokens  : {tokens}")
        print("=" * 50)

chunker = UniversalChunker(chunk_size=300, overlap=30)

chunks = chunker.chunk(
    text=SAMPLE_TEXT,
    source="sample",
    strategy="recursive"
)

chunker.stats(chunks)
'''

'''
# First Collection

import chromadb


client = chromadb.Client()


client = chromadb.PersistentClient(path="./chroma_db")


collection = client.create_collection(
    name="ai_knowledge",
)

print("Collection created:", collection.name)
'''

'''

# Adding Documents in the collection

import chromadb
from google import genai

client_ai  = genai.Client()
client_db  = chromadb.PersistentClient(path="./chroma_db")

collection = client_db.get_or_create_collection(
    name="ai_knowledge"
)


def embed(text: str) -> list[float]:
    response = client_ai.models.embed_content(
        model="models/gemini-embedding-001",
        contents=text
    )
    return response.embeddings[0].values


chunks = [
    {
        "id":   "chunk_0",
        "text": "RAG stands for Retrieval Augmented Generation. "
                "It combines LLMs with external knowledge bases "
                "to reduce hallucination.",
        "metadata": {"source": "ai_overview.txt", 
        "topic": "RAG",
        "difficulty": "intermediate"
        }
    },
    {
        "id":   "chunk_1",
        "text": "ChromaDB is a free, open-source vector database. "
                "It stores embeddings and enables fast similarity "
                "search for RAG systems.",
        "metadata": {"source": "ai_overview.txt",
         "topic": "ChromaDB",
        "difficulty": "biginner"
         }
    },
    {
        "id":   "chunk_2",
        "text": "Embeddings are vector representations of text. "
                "Similar meanings produce similar vectors. "
                "Cosine similarity measures closeness.",
        "metadata": {
        "source": "ai_overview.txt", 
        "topic": "Embeddings",
        "difficulty": "intermediate"
        }
    },
    {
        "id":   "chunk_3",
        "text": "LangGraph is a framework for building stateful "
                "multi-agent workflows as graphs. Nodes are agents "
                "or tools. Edges define information flow.",
        "metadata": {
        "source": "ai_overview.txt", 
        "topic": "LangGraph",
        "difficulty": "advanced"
        }
    },
    {
        "id":   "chunk_4",
        "text": "Prompt engineering is the skill of designing inputs "
                "to LLMs to get reliable outputs. Techniques include "
                "zero-shot, few-shot, and chain of thought.",
        "metadata": {
        "source": "ai_overview.txt", 
        "topic": "Prompting",
        "difficulty": "beginner"
        }
    },
     {
        "id": "chunk_5",
        "text": "Agentic AI refers to AI systems that can reason, plan, and take actions autonomously to achieve goals. They combine large language models with memory, tools, and decision-making loops to solve multi-step tasks.",
        "metadata": {
            "source": "ai_overview.txt",
            "topic": "Agentic AI",
            "difficulty": "beginner"
        }
    },
    {
        "id": "chunk_6",
        "text": "Tool calling enables a language model to invoke external functions or APIs when additional information or computation is required. The model decides which tool to use based on the user's request and integrates the result into its response.",
        "metadata": {
            "source": "ai_overview.txt",
            "topic": "Tool Calling",
            "difficulty": "advanced"
        }
    },
    {
        "id": "chunk_7",
        "text": "Vector databases store high-dimensional embedding vectors and perform fast similarity searches. Popular vector databases include ChromaDB, Pinecone, Weaviate, Milvus, and FAISS. They are widely used in Retrieval-Augmented Generation systems.",
        "metadata": {
            "source": "ai_overview.txt",
            "topic": "Vector Databases",
            "difficulty": "intermediate"
        }
    },
    {
        "id": "chunk_8",
        "text": "Fine-tuning modifies a model's parameters using additional training data, while Retrieval-Augmented Generation keeps the model unchanged and retrieves relevant external documents during inference. RAG is generally faster and easier to update with new knowledge.",
        "metadata": {
            "source": "ai_overview.txt",
            "topic": "Fine-tuning vs RAG",
            "difficulty": "beginner"
        }
    },
    {
        "id": "chunk_9",
        "text": "Python is the most popular programming language for AI Engineering because of its simple syntax and rich ecosystem. Libraries such as NumPy, Pandas, PyTorch, TensorFlow, LangChain, and Google GenAI SDK help developers build intelligent applications efficiently.",
        "metadata": {
            "source": "ai_overview.txt",
            "topic": "Python for AI Engineering",
            
        }
    },
]


print("Embedding and storing chunks...")

collection.add(
    ids        = [c["id"]       for c in chunks],
    documents  = [c["text"]     for c in chunks],
    embeddings = [embed(c["text"]) for c in chunks],
    metadatas  = [c["metadata"] for c in chunks],
)

print(f"Stored {collection.count()} chunks.")

print(f"\nTotal chunks in collection: {collection.count()}")

print("\nStored Chunk IDs:")
ids = collection.get()["ids"]

for chunk_id in ids:
    print(chunk_id)
'''
'''
# Semantic Search

import chromadb
from google import genai

client_ai  = genai.Client()
client_db  = chromadb.PersistentClient(path="./chroma_db")

collection = client_db.get_or_create_collection(
    name="ai_knowledge"
)

def embed(text: str) -> list[float]:
    response = client_ai.models.embed_content(
        model="models/gemini-embedding-001",
        contents=text
    )
    return response.embeddings[0].values

def search(query: str, n_results: int = 3) -> list[dict]:
   
    query_embedding = embed(query)

    results = collection.query(
        query_embeddings = [query_embedding],
        n_results        = n_results,
        include          = ["documents", "metadatas", "distances"]
    )

   
    output = []
    for i in range(len(results["ids"][0])):
        output.append({
            "id":       results["ids"][0][i],
            "text":     results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": round(results["distances"][0][i], 4),
        })

    return output



query   = "How do I store embeddings?"
results = search(query, n_results=2)

print(f"Query: {query}\n")
for r in results:    
    print(f"ID:       {r['id']}")
    print(f"Distance: {r['distance']}  (lower = more similar)")
    print(f"Topic:    {r['metadata']['topic']}")
    print(f"Text:     {r['text'][:80]}...")
    print("─" * 40)



# filtering with MetaData



results = collection.query(
    query_embeddings = [embed("explain AI concepts")],
    n_results        = 3,
    where            = {"difficulty": "beginner"},  
    include          = ["documents", "metadatas", "distances"]
)

print(results["documents"])

for i in range(len(results["ids"][0])):
    print(f"ID: {results['ids'][0][i]}")
    print(f"Topic: {results['metadatas'][0][i]['topic']}")
    print(f"Difficulty: {results['metadatas'][0][i]['difficulty']}")
    print(f"Distance: {results['distances'][0][i]}")
    print(f"Text: {results['documents'][0][i]}")
    print("-" * 50)


resultss = collection.query(
    query_embeddings = [embed("AI tools and frameworks")],
    n_results        = 3,
    where            = {
        "$and": [
            {"source":  {"$eq": "ai_overview.txt"}},
            {"topic":   {"$in": ["RAG", "LangGraph", "Prompting"]}}
        ]
    },
    include = ["documents", "metadatas", "distances"]
)


# Updating And Deleting Chunk

collection.update(
    ids        = ["chunk_0"],
    documents  = ["RAG (Retrieval Augmented Generation) is a "
                  "technique that combines LLMs with vector "
                  "databases to ground responses in real data."],
    embeddings = [embed("RAG is a technique that combines LLMs "
                        "with vector databases...")],
    metadatas  = [{"source": "ai_overview.txt", "topic": "RAG",
                   "difficulty": "intermediate", "updated": True}]
)


collection.delete(ids=["chunk_3"])


print("Chunks remaining:", collection.count())


result = collection.get(
    ids     = ["chunk_0"],
    include = ["documents", "metadatas"]
)
print(result)


# Collection Management All the operations

# List all collections
collections = client_db.list_collections()
for col in collections:
    print(col.name)

# Delete all collections
client_db.delete_collection("ai_knowledge")

# Get or create a collection safe for production
collection = client_db.get_or_create_collection(
    name     = "ai_knowledge",
    metadata = {"description": "AI Engineering knowledge base"}
)

# Peek at stored data
peek = collection.peek(limit=3)
print(peek["ids"])
print(peek["documents"])

'''

'''
# All together of chromaDb operations

import chromadb
from google import genai

client_ai = genai.Client()
client_db = chromadb.PersistentClient(path="./chroma_db")

def embed(text: str) -> list[float]:
    response = client_ai.models.embed_content(
        model    = "models/gemini-embedding-001",
        contents = text
    )
    return response.embeddings[0].values


class KnowledgeBase:

    def __init__(self, name: str):
        self.collection = client_db.get_or_create_collection(name)
        print(f"KB '{name}' ready. Chunks: {self.collection.count()}")

    def add(self, chunks: list[dict]):
        
        self.collection.add(
            ids        = [c["id"]          for c in chunks],
            documents  = [c["text"]        for c in chunks],
            embeddings = [embed(c["text"]) for c in chunks],
            metadatas  = [c["metadata"]    for c in chunks],
        )
        print(f"Added {len(chunks)} chunks. Total: {self.collection.count()}")

    def search(self, query: str, n: int = 3, filters: dict = None) -> list[dict]:
        kwargs = {
            "query_embeddings": [embed(query)],
            "n_results":        n,
            "include":          ["documents", "metadatas", "distances"]
        }
        if filters:
            kwargs["where"] = filters

        results = self.collection.query(**kwargs)

        return [
            {
                "text":     results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "score":    round(1 - results["distances"][0][i], 4),
            }
            for i in range(len(results["ids"][0]))
        ]

    def count(self) -> int:
        return self.collection.count()

    def remove(self, id: str):
        try:
            self.collection.delete(ids=[id])
            print(f"Chunk '{id}' deleted successfully.")

        except Exception as e:
            print(f"Error deleting chunk: {e}")
    
    def update(self, id: str, new_text: str, new_metadata: dict):
        try:
            self.collection.update(
                ids        = [id],
                documents  = [new_text],
                embeddings=[embed(new_text)],
                metadatas  = [new_metadata]
                            )
            print(f"New Chunk Added {id}")
        
        except Exception as e:
            print(f"Error adding chunkl : {e}")



kb = KnowledgeBase("ai_knowledge_v2")

kb.add([
    {
        "id":   "rag_intro",
        "text": "RAG combines LLMs with vector databases to "
                "ground responses in real documents.",
        "metadata": {"topic": "RAG", "difficulty": "beginner"}
    },
    {
        "id":   "chroma_intro",
        "text": "ChromaDB is a local vector database for storing "
                "and searching embeddings in RAG systems.",
        "metadata": {"topic": "ChromaDB", "difficulty": "beginner"}
    },
    {
        "id":   "agent_intro",
        "text": "AI agents use tools in a loop to complete tasks "
                "autonomously without human intervention.",
        "metadata": {"topic": "Agents", "difficulty": "intermediate"}
    },
])


results = kb.search("how does RAG reduce hallucination?", n=2)

for r in results:
    print(f"Score:    {r['score']}  (higher = more similar)")
    print(f"Topic:    {r['metadata']['topic']}")
    print(f"Text:     {r['text']}")
    print("─" * 40)

kb.add([
    {
        "id": "python_intro",
        "text": "Python is the most popular language for AI Engineering.",
        "metadata": {
            "topic": "Python",
            "difficulty": "beginner"
        }
    }
])

kb.update(
    id="chroma_intro",
    new_text="ChromaDB is an open-source vector database used for semantic search and Retrieval-Augmented Generation applications.",
    new_metadata={
        "topic": "ChromaDB",
        "difficulty": "beginner"
    }
)

kb.remove("agent_intro")

results = kb.search("What is ChromaDB?")

for r in results:
    print(r)
'''
# Final Assesment Module 20
import chromadb
from google import genai

client_ai = genai.Client()
client_db = chromadb.PersistentClient(path="./chroma_db")

def embed(text: str) -> list[float]:
    response = client_ai.models.embed_content(
        model    = "models/gemini-embedding-001",
        contents = text
    )
    return response.embeddings[0].values


class KnowledgeBase:

    def __init__(self, name: str):
        self.collection = client_db.get_or_create_collection(name)
        print(f"KB '{name}' ready. Chunks: {self.collection.count()}")

    def add(self, chunks: list[dict]):
        
        self.collection.add(
            ids        = [c["id"]          for c in chunks],
            documents  = [c["text"]        for c in chunks],
            embeddings = [embed(c["text"]) for c in chunks],
            metadatas  = [c["metadata"]    for c in chunks],
        )
        print(f"Added {len(chunks)} chunks. Total: {self.collection.count()}")

    def search(self, query: str, n: int = 3, filters: dict = None) -> list[dict]:
        kwargs = {
            "query_embeddings": [embed(query)],
            "n_results":        n,
            "include":          ["documents", "metadatas", "distances"]
        }
        if filters:
            kwargs["where"] = filters

        results = self.collection.query(**kwargs)

        return [
            {
                "text":     results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "score":    round(1 - results["distances"][0][i], 4),
            }
            for i in range(len(results["ids"][0]))
        ]

    def count(self) -> int:
        return self.collection.count()

    def remove(self, id: str):
        try:
            self.collection.delete(ids=[id])
            print(f"Chunk '{id}' deleted successfully.")

        except Exception as e:
            print(f"Error deleting chunk: {e}")
    
    def update(self, id: str, new_text: str, new_metadata: dict):
        try:
            self.collection.update(
                ids        = [id],
                documents  = [new_text],
                embeddings=[embed(new_text)],
                metadatas  = [new_metadata]
                            )
            print(f"New Chunk Added {id}")
        
        except Exception as e:
            print(f"Error adding chunkl : {e}")



kb = KnowledgeBase("Phase_2")

kb.add([
    {
        "id":   "Module 11",
        "text": """ LLM stands for Large Language Model, A neural network
        trained on massive amounts of text.
        That learns to pridict the next token given previous tokens.
        
        
        LLMs are built on the transformer architecture.
        -> Attention mechanism
        -> Every word looks at every other word simulaneously.
        -> Parallel processing = Fast
        -> Long range context = no forgetting
        
        
        How Trainig works ?
        step 1: collect data
        step 2: Tokenize
        step 3: Train
        step 4: RLHF (Reinforcement learning from Human feedback)
        
        
        What happens when API is called ?
        
        promt -> Tokenizer -> Embedding layer -> Transformer layers -> output layer -> sampling -> Next token -> Full Response
        
        
        -> Tokens are not words, not characters. is a sub word units
        e.g. "unhappiness" -> [un , happiness] (2 tokens)
        
        -> Context window is a models's working memory,
        everything it can see at once.
        
        -> Embeddings is a method where text converted into vectors.
        
        -> Temperature controls randomness of output,
        it always pick highers probability token.
        
        -> Hallucinations is the model confidently states false information.
        """,
        "metadata": {"topic": "LLM", "difficulty": "beginner"}
    },
    {
        "id":   "Module 12",
        "text": """ Tokenuization is the process of converting raw text into
        numbers the model can process.
        
        Context Window is maximum tokens the model can see in one API call.
        
        Embeddings is the process where text converted into vectors that 
        capture meaning.
        
        
        Working of the Tokenization.
        It works on the principal of Byte Pair Encoding.
        Rules:
        -> spaces, caps, `punctuation = affect token count,
        -> Non-English text = More tokens,
        -> Numbers & code = often expensive in tokens
        
        
        setup:
        'pip install tiktoken openai numpy'
        
        tokentization(code):
        import tiktoken
        enc= tiketoken.encoding_for_model("gpt")
        text = "Hello, My name is Om"
        
        tokens = enc.encode(text)
        
        print("Token IDs:", tokens)
        print("Token count:", len(tokens))
        print("Decoded: ", enc.decode(tokens)) 
        """,
        "metadata": {"topic": "Tokenization", "difficulty": "intermidiate"}
    },
    {
        "id":   "Module 13",
        "text": """ 
        The skill of desiginig inputs to an LLM to get reliable,
        accurate and useful outputs.

        Why it exists :-
        the models's output quality is directly controlled by the quality of
        your input.

        Message Structure :-
        LLM Api call has 3 roles-
        1 -> System: sets behaviour, Persona, rules
        2 -> User: The human input
        3 -> Assistant -> The model's response (in History)

        Types of Prompting :-

        1 -> Zero shot prompting
            Give the model a task with no examples.
            When to use:
                Simple, well known tasks
                Model already understands the domain
                Fast iteration

        2 -> Few shot prompting
            Give the model examples before the task.
            Show it the pattern you want.
            When to use:
                Custom output formats
                Tasks the model get wrong with zero Shot
                consitent structured outputs

        3 -> ChainOfThoughts (COT)
            Force the model to think step by step before giving the final response.

        3 -> ReAct Prompting
            React = Reasoning + Acting
            The model:
                Thinks about what to do (reasoning)
                Decides an action
                observes the result
                Repeat until done

            format:
                Thought - [What model is thinking]
                Action - [What tool/step to take]
                Observation - [Result of the action]
                ...repeat...
                Final answer - [conclusion]
        
        4 -> System Prompt Engineering
            A system prompt is your product.
            A well engineered system prompt has:
                1. Persona: Who the model is
                2. Goal: what it must do
                3. Constraints: what it must not do
                4. Format: How output should look
                5. Tone: How it should sound
                6. Edge cases: What to do when unsure
        """,
        "metadata": {"topic": "Prompt Engineering", "difficulty": "beginner"}
    },
    {
        "id":   "Module 14",
        "text": """ 
        Structure output:
            Forcing the LLm to respond in a spesific, predictable, machine
            readable format.
            Instead of:
                "The user seems to be feeling sad and stressed"
            you get:
                {
                "emotion" : "sad",
                "confidence" : 0.91,
                "reqwuires_followup" : true
                }

            why it exists :
                LLM outputs are text by difault. Text is unpredictable.
                Machines need structure.

            Probles without structured output:
                you ask for json
                    "Here is the json"
                You parse it
                    Your code crashes
                Output format changes randomly between calls
                Production system break

            Solution ;
                Forece the model to output ONLY valid structure
                Your code can reliably parse it every time
                Build real applications on top of LLM outputs

            Where To use:
                Resume Paper :- extract.name, skills, experience
                Sentiment API :- {emotion, score, category}
                code Reviewer :- {score, reasons, next_action}
                RAG System ;- {answer, source[], confidence}

        Types Of the Structured Output ->
            Simplest approach. Tell the model to respond in JSON.
            NO special API features needed. works with any model.

            code:
                from google import genai
                client = genai.Client()

                prompt = 'sample prompt with format : {
                "name" : "string",
                "age" : number,
                "skills" : ["string"]
                }
        """,
        "metadata": {"topic": "Structured Output", "difficulty": "advanced"}
    }
])


results = kb.search("How do I make an LLM use external tools?", n=2)

for r in results:
    print(f"Score:    {r['score']}  (higher = more similar)")
    print(f"Topic:    {r['metadata']['topic']}")
    print(f"Text:     {r['text']}")
    print("─" * 40)
'''
kb.add([
    {
        "id": "python_intro",
        "text": "Python is the most popular language for AI Engineering.",
        "metadata": {
            "topic": "Python",
            "difficulty": "beginner"
        }
    }
])

kb.update(
    id="chroma_intro",
    new_text="ChromaDB is an open-source vector database used for semantic search and Retrieval-Augmented Generation applications.",
    new_metadata={
        "topic": "ChromaDB",
        "difficulty": "beginner"
    }
)

kb.remove("agent_intro")

results = kb.search("What is ChromaDB?")

for r in results:
    print(r)
'''