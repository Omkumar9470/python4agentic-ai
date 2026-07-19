from google import genai
from google.genai import types

from config       import GEMINI_API_KEY, MODEL, SYSTEM_PROMPT
from memory       import ConversationMemory
from tools        import TOOLS, execute_tool

import time

client = genai.Client(api_key=GEMINI_API_KEY)


def get_response(memory: ConversationMemory) -> str:

    recent   = memory.get_recent()
    full_reply = ""

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=recent,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=[TOOLS]
            )
        )

        part = response.candidates[0].content.parts[0]

        if part.function_call:
            fn_name = part.function_call.name
            fn_args = dict(part.function_call.args)

            print(f"\n  [Tool: {fn_name}({fn_args})]")

            result = execute_tool(fn_name, fn_args)

            messages_with_tool = [
                *recent,
                response.candidates[0].content,
                types.Content(
                    role="user",
                    parts=[
                        types.Part(
                            function_response=types.FunctionResponse(
                                name=fn_name,
                                response=result
                            )
                        )
                    ]
                )
            ]

            print("Aria: ", end="", flush=True)

            for chunk in client.models.generate_content_stream(
                model=MODEL,
                contents=messages_with_tool,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    tools=[TOOLS]
                )
            ):
                if chunk.text:
                    print(chunk.text, end="", flush=True)
                    full_reply += chunk.text

        else:
            print("Aria: ", end="", flush=True)

            for chunk in client.models.generate_content_stream(
                model=MODEL,
                contents=recent,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    tools=[TOOLS]
                )
            ):
                if chunk.text:
                    print(chunk.text, end="", flush=True)
                    full_reply += chunk.text

        print()
        return full_reply

    except Exception as e:
        print(f"\n  [Error: {e}. Retrying in 20s...]")
        time.sleep(20)

        try:
            print("Aria: ", end="", flush=True)

            for chunk in client.models.generate_content_stream(
                model=MODEL,
                contents=recent,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT
                )
            ):
                if chunk.text:
                    print(chunk.text, end="", flush=True)
                    full_reply += chunk.text

            print()
            return full_reply

        except Exception as e2:
            msg = f"Sorry, I'm having trouble connecting. ({e2})"
            print(msg)
            return msg