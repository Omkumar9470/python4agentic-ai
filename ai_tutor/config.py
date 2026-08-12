import os
from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
    _HAS_STREAMLIT = True
except ImportError:
    _HAS_STREAMLIT = False


def _get_secret(key: str, default: str = "") -> str:
    if _HAS_STREAMLIT:
        try:
            if key in st.secrets:
                return st.secrets[key]
        except Exception:
            pass
    return os.getenv(key, default)

GEMINI_API_KEY = _get_secret("GEMINI_API_KEY", "")
MODEL           = "gemini-2.5-flash"


MAX_HISTORY_MESSAGES = 10   


SYSTEM_PROMPT = """
You are an expert AI Engineering tutor named Aria.
You are helping Om, a final-year CS student,
master AI Engineering to get a job.

Your rules:
- Always explain concepts before showing code
- Use bullet points, not long paragraphs
- Give real-world examples from AI Engineering
- When writing code, add comments on each line
- If asked something outside AI/tech, redirect politely
- Keep answers concise and structured
- Never skip the 'why' behind any concept

Current learning phase: LLM Engineering (Phase 2 of 10)
""".strip()

# Commands
COMMANDS = {
    "/help":    "Show available commands",
    "/clear":   "Reset conversation history",
    "/history": "Show number of turns so far",
    "/export":  "Save conversation to a file",
    "/quit":    "Exit the chat",
}