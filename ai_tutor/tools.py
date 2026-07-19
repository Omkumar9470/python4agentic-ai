from datetime import datetime
from google.genai import types



def get_current_date(timezone: str = "IST") -> dict:
    now = datetime.now()
    return {
        "date":     now.strftime("%Y-%m-%d"),
        "time":     now.strftime("%H:%M:%S"),
        "day":      now.strftime("%A"),
        "timezone": timezone
    }


def search_ai_topics(topic: str) -> dict:
    knowledge = {
        "rag": (
            "RAG = Retrieval Augmented Generation. "
            "Combines LLMs with external knowledge bases "
            "to reduce hallucinations and add real-time data."
        ),
        "agent": (
            "AI Agent = LLM + Tools + Loop. "
            "The model reasons, calls tools, observes results, "
            "and repeats until the task is complete."
        ),
        "embedding": (
            "Embeddings are vector representations of text. "
            "Similar meanings = similar vectors. "
            "Used in RAG for semantic search."
        ),
        "langchain": (
            "LangChain is a framework for building LLM apps. "
            "Provides chains, agents, memory, and tool integrations."
        ),
        "langgraph": (
            "LangGraph builds stateful multi-agent workflows "
            "as graphs. Nodes = agents/tools. Edges = flow."
        ),
        "transformer": (
            "Transformer is the neural architecture behind LLMs. "
            "Key innovation: attention mechanism that lets every "
            "token attend to every other token simultaneously."
        ),
    }

    topic_lower = topic.lower()
    for key, value in knowledge.items():
        if key in topic_lower:
            return {"found": True, "topic": topic, "content": value}

    return {
        "found":   False,
        "topic":   topic,
        "content": f"No entry found for '{topic}'. Try: "
                   "rag, agent, embedding, langchain, langgraph, transformer"
    }



def execute_tool(name: str, args: dict) -> dict:
    if name == "get_current_date":
        return get_current_date(**args)
    elif name == "search_ai_topics":
        return search_ai_topics(**args)
    return {"error": f"Unknown tool: {name}"}



TOOLS = types.Tool(
    function_declarations=[
        {
            "name": "get_current_date",
            "description": "Get the current date, time, and day",
            "parameters": {
                "type": "object",
                "properties": {
                    "timezone": {
                        "type": "string",
                        "description": "Timezone abbreviation e.g. IST, UTC"
                    }
                },
                "required": []
            }
        },
        {
            "name": "search_ai_topics",
            "description": (
                "Search the AI Engineering knowledge base "
                "for definitions and explanations of AI topics"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "AI topic to search e.g. RAG, agent, embedding"
                    }
                },
                "required": ["topic"]
            }
        }
    ]
)