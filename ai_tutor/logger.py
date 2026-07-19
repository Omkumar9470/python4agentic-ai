import json
import os
from datetime import datetime


LOG_DIR = "logs"


def ensure_log_dir():
    os.makedirs(LOG_DIR, exist_ok=True)


def export_conversation(messages, turn_count):

    ensure_log_dir()

    export_messages = []

    for message in messages:

        parts = []

        for part in message.parts:
            parts.append(part.text)

        export_messages.append(
            {
                "role": message.role,
                "parts": parts
            }
        )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{LOG_DIR}/chat_{timestamp}.json"

    log = {
        "exported_at": datetime.now().isoformat(),
        "turn_count": turn_count,
        "messages": export_messages
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=4, ensure_ascii=False)

    return filename