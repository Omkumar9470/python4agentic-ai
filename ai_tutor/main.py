from config  import COMMANDS
from memory  import ConversationMemory
from chat    import get_response
from logger  import export_conversation


def print_banner():
    print("=" * 50)
    print("   Aria — AI Engineering Tutor")
    print("   Phase 2: LLM Engineering")
    print("   Type /help for commands")
    print("=" * 50)
    print()


def handle_command(cmd: str, memory: ConversationMemory) -> bool:

    if cmd == "/help":
        print("\nAvailable commands:")
        for command, desc in COMMANDS.items():
            print(f"  {command:<12} → {desc}")
        print()
        return True

    elif cmd == "/clear":
        memory.clear()
        print("\n[History cleared. Starting fresh.]\n")
        return True

    elif cmd == "/history":
        print(f"\n[{memory.summary()}]\n")
        return True

    elif cmd == "/export":
        filename = export_conversation(
            memory.messages,
            memory.turn_count
        )
        print(f"\n[Conversation exported to: {filename}]\n")
        return True

    elif cmd == "/quit":
        print("\nGoodbye! Keep building. 🚀\n")
        exit(0)

    return False


def main():
    print_banner()

    memory = ConversationMemory()

    while True:

        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nGoodbye!\n")
            break

        if not user_input:
            continue

        if user_input.startswith("/"):
            handle_command(user_input.lower(), memory)
            continue

        memory.add_user(user_input)

        reply = get_response(memory)

        memory.add_model(reply)

        print(f"  [{memory.summary()}]\n")


if __name__ == "__main__":
    main()