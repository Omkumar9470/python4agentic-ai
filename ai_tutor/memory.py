from google.genai import types
from config import MAX_HISTORY_MESSAGES


class ConversationMemory:

    def __init__(self):
        self.messages = []
        self.turn_count = 0

    def add_user(self, text: str):
        self.messages.append(
            types.Content(
                role="user",
                parts=[
                    types.Part(text=text)
                ]
            )
        )
        self.turn_count += 1

    def add_model(self, text: str):
        self.messages.append(
            types.Content(
                role="model",
                parts=[
                    types.Part(text=text)
                ]
            )
        )

    def get_recent(self):
        return self.messages[-MAX_HISTORY_MESSAGES:]

    def clear(self):
        self.messages = []
        self.turn_count = 0

    def token_estimate(self) -> int:
        total_chars = 0

        for message in self.messages:
            for part in message.parts:
                if part.text:
                    total_chars += len(part.text)

        return total_chars // 4

    def summary(self):
        return (
            f"Turns: {self.turn_count} | "
            f"Messages in memory: {len(self.messages)} | "
            f"Tokens (approx): ~{self.token_estimate()}"
        )