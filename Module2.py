'''
# Tokenization

import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text1 = "Hello i am using python!"
text2 = "नमस्ते, मैं Python का इस्तेमाल कर रहा हूँ!"
text3 = "print('Token ID:' , tokens1)"

tokens1 = enc.encode(text1)
tokens2 = enc.encode(text2)
tokens3 = enc.encode(text3)

print("Token ID: ", tokens1)
print("Token Count: ", len(tokens1))
print("Decoded : ", enc.decode(tokens1))

print("Token ID: ", tokens2)
print("Token Count: ", len(tokens2))
print("Decoded : ", enc.decode(tokens2))

print("Token ID: ", tokens3)
print("Token Count: ", len(tokens3))
print("Decoded : ", enc.decode(tokens3))

'''

'''
# Token Counter

import tiktoken

def count_tokens (text: str, model: str = "gpt-4o") -> int:
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))

def count_message_tokens (messages: list) -> int:
    enc = tiktoken.encoding_for_model("gpt-4o")
    total = 0

    for message in messages:
        total += 4
        for value in message.values():
            total += len(enc.encode(value))
    
    total += 2
    return total

text = "Hello my name is Om Pandey"

chat_history = [
    {
        "role": "system", 
        "content": "You are a precise math tutor assistant."
    },
    {
        "role": "user", 
        "content": "What is 2 + 2?"
    },
    {
        "role": "assistant", 
        "content": "2 + 2 equals 4."
    }
]

print(count_tokens(text))
print(count_message_tokens(chat_history))
'''

'''

import google.generativeai as genai
import time

genai.configure()

model = genai.GenerativeModel("gemini-2.5-flash")


def count_history_chars(history: list) -> int:
    total = 0
    for message in history:
        for part in message["parts"]:
            total += len(part)
    return total

def chat(user_input: str, history: list, max_messages: int = 10) -> tuple:

    # Sliding window — keep last N messages
    if len(history) > max_messages:
        history = history[-max_messages:]

    # Add new user message
    history.append({
        "role": "user",
        "parts": [user_input]
    })

    print(f"  [History size: {len(history)} messages, "
          f"~{count_history_chars(history)} chars]")
    
    response = model.generate_content(history)

    reply = response.text

    
    history.append({
        "role": "model",
        "parts": [reply]
    })

    return reply, history



history = []

turns = [
    "My name is Om",
    "I am a final year CS student",
    "I am learning Agentic AI",
    "I want to get a job as an AI Engineer",
    "Summarize everything you know about me"
]

for turn in turns:
    time.sleep(15)
    print(f"You: {turn}")
    reply, history = chat(turn, history)
    print(f"Bot: {reply[:80]}...")
    print()

'''
'''

# Test Prompts

from google import genai
from google.genai import types
import time

client = genai.Client()

def chat(prompt: str) -> str:

    try:
        response = client.models.generate_content(
            model = 'gemini-2.5-flash',
            contents = prompt,
            config = types.GenerateContentConfig(
                system_instruction ="You are a professional chatbot that build to answer coding questions. but don not give output more than 500 words"
            )
        )
        return response.text

    except Exception as e:
        return f"An Error occurered: {e}"

prompt_a = chat("explain async and await in python")
print(prompt_a)
time.sleep(15)

prompt_b = chat("explain async and await in python. use bullet points to make it more understandable. and do not give unessary explainations")
print(prompt_b)
time.sleep(15)

prompt_c = chat("explain async and await in python. use bullet points to make it more understandable. and do not give unessary explainations. imagine you as a proffesor of MIT give output as a structure course and look it more proffesional not ai generated.")
print(prompt_c)

'''

'''

# Personal Ai Tutor

from google import genai
from google.genai import types

client = genai.Client()


def chat (prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model= 'gemini-2.5-flash',
            contents= prompt,
            config= types.GenerateContentConfig(system_instruction= """
            You are professor of AI Engineering, You are so good that every student want to learn from you.
            You Have to teach Om a btech-cs graduate agentic ai so he can get a job as soon as possible.
            Do not give longer explainations. do not go out of the topic just only learnings.
            you give answers in bullets points so it can be more easy to remember visually.
            You soud take a proffesional and strict tone as a professor but not that much.
            whenever you are not sure what is asked by the user, just tell to clarify their need.
            """)
        )
        return response.text

    except Exception as e:
        return f"An error occurered: {e}"

while True:
    print("Chat with ai tutor")

    user_input = input("you: ")

    print(chat(user_input))

    print("Want to continue? y/n")
    choice = input("-> ")
    if choice == 'n':
        break
    elif choice == 'y':
        continue

'''
'''

# Personal AI Tutor Advanced

from google import genai
from google.genai import types

client = genai.Client()


history = []

SYSTEM_PROMPT = """
Persona:
You are a Professor of AI Engineering with 15 years of teaching experience.

Goal:
Teach Om Agentic AI so he can become job-ready as quickly as possible.

Constraints:
- Teach only Agentic AI topics.
- Keep explanations short.
- Do not go off-topic.

Format:
Always answer in this format:

Topic:
Definition:
Key Points:
Example:
Interview Tip:

Tone:
Professional, friendly, and slightly strict.

Edge Cases:
If the user's question is unclear, ask for clarification instead of guessing.

Example:

User: What is Prompt Engineering?

Assistant:

Topic:
Prompt Engineering

Definition:
Writing effective instructions for an AI model.

Key Points:
- Better prompts give better outputs.
- Used in AI applications.
- Important for Agentic AI.

Example:
"Explain Python in simple words."

Interview Tip:
Be able to explain why prompt quality affects AI responses.
"""


def chat(prompt: str) -> str:
    try:

        history.append(
            types.Content(
                role="user",
                parts=[types.Part(text=prompt)]
            )
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=history,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

        history.append(
            types.Content(
                role="model",
                parts=[types.Part(text=response.text)]
            )
        )

    
        if len(history) > 6:
            history[:] = history[-6:]

        return response.text

    except Exception as e:
        return f"Error: {e}"


print("===== Personal AI Tutor =====")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    print("\nTutor:")
    print(chat(user_input))

'''

'''

# Extract Job Postings

from google import genai
from google.genai import types
import json

client = genai.Client()

def extract_job_posting (text : str) -> dict:
    prompt = f""" 
    Extract Information and return only valid json.
    No explaination, No codes, nothing else.
    format :
    {{
        "company" : "string",
        "role" : "string",
        "required_skills" : ["string"],
        "experience_years" : number,
        "remote" : boolean
    }}
    Text : {text}
    """

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )

    raw = response.text.strip()

    if raw.startswith("```"):
        raw = raw.split("```") [1]
        if raw.startswith("json"):
            raw = raw[4:]

    return json.loads(raw)

test = """TechCorp is hiring a Senior AI Engineer with 3+ years
of experience. Must know Python, LangChain, and 
vector databases. This is a fully remote position."""

results = extract_job_posting(test)

result = extract_job_posting(test)

print(f"Company: {result['company']}")
print(f"Role: {result['role']}")
print(f"Required Skills: {result['required_skills']}")
print(f"Experience Years: {result['experience_years']}")
print(f"Remote: {result['remote']}")

'''

'''

# Extract Job Posting Using Json Mode

from google import genai
from google.genai import types
import json

client = genai.Client()

def extract_job_posting(text: str) -> dict:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            system_instruction="""
                Extract the following information from the job posting 
                and return valid JSON:

                {
                    "company": "string",
                    "role": "string",
                    "required_skills": ["string"],
                    "experience_years": number,
                    "remote": boolean
                }
            """
        )
    )

    return json.loads(response.text)


text = """TechCorp is hiring a Senior AI Engineer with 3+ years
of experience. Must know Python, LangChain, and
vector databases. This is a fully remote position."""

print(extract_job_posting(text))
'''

'''
# Resume_Parser

from google import genai
from google.genai import types
import json

client = genai.Client()

def resume_parser (resume_text: str) -> list:
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = resume_text,
        config = types.GenerateContentConfig(
            response_mime_type = "application/json",
            system_instruction = """ 
            Extract all the information from the resume text.
            Return only a valid JSON object in this format:
            {
                "name": "string",
                "email": "string or null",
                "education": [
                    {
                        "degree": "string",
                        "institution": "string",
                        "year": "string"
                    }
                ],
                "experience": [
                    {
                        "role": "string",
                        "company": "string",
                        "duration": "string"
                    }
                ],
                "skills": ["string"]
            }
            Do not return explanations or Markdown.
            """
        )
    )
    return json.loads(response.text)

resume_text = """
Om Kumar
Email: omkumar@example.com

Bachelor of Technology in Computer Science, APJ Abdul Kalam Technical University, 2025

Software Developer Intern at TechNova Solutions (Jan 2024 - Jun 2024)

Skills: Python, JavaScript, React, Node.js, LangChain, SQL
"""

items = resume_parser(resume_text)

print(json.dumps(items, indent=4))
'''

'''
# job_fit_analyzer

from google import genai
from google.genai import types
import json

client = genai.Client()

def job_fit_analyzer (j_d: str, cand_profile: str) -> dict:
    response = client.models.generate_content(
        model= "gemini-2.5-flash",
        contents= cand_profile,
        config= types.GenerateContentConfig(
            response_mime_type = "application/json",
            system_instruction = f""" 
            Analyse the candidate profile for the role {j_d}
            and return a valid json
            {{
                "fit_score": 0 to 100,
                "matching_skills": ["string"],
                "missing_skills": ["string"],
                "recommendation": "strong_fit|possible_fit|weak_fit",
                "summary": "string"
            }}
            """
        )        
    )
    return json.loads(response.text)

job = "AI Engineer — needs Python, LangChain, RAG, vector DBs, FastAPI, 2+ years exp"

candidate = "Om, final year CS student, knows Python, Next.js, Gemini API, has 2 freelance projects, currently learning LangChain and RAG"

result = job_fit_analyzer(job, candidate)

print(json.dumps(result, indent=4))
'''

'''
# Using Tool For Weather

from google import genai
from google.genai import types
import time

client = genai.Client()


# ---------------- Weather Function ----------------
def get_weather(city: str) -> dict:
    weather_data = {
        "Delhi": {"temp": 38, "condition": "Sunny"},
        "Mumbai": {"temp": 30, "condition": "Humid"},
        "Bangalore": {"temp": 24, "condition": "Cloudy"},
        "Chennai": {"temp": 34, "condition": "Rainy"},
        "Noida": {"temp": 36, "condition": "Hazy"}
    }

    city = city.title()

    return weather_data.get(
        city,
        {"temp": 0, "condition": "Unknown"}
    )


# ---------------- Tool Definition ----------------
weather_tool = types.Tool(
    function_declarations=[
        {
            "name": "get_weather",
            "description": "Get current weather for an Indian city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    ]
)


# ---------------- Agent ----------------
def ask_weather(user_query: str):

    # First Request
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_query,
        config=types.GenerateContentConfig(
            tools=[weather_tool]
        )
    )

    part = response.candidates[0].content.parts[0]

    # Model answered directly
    if not getattr(part, "function_call", None):
        return part.text

    fn_name = part.function_call.name
    fn_args = dict(part.function_call.args)

    print(f"\nTool Called : {fn_name}")
    print(f"Arguments   : {fn_args}")

    # Execute Tool
    result = get_weather(**fn_args)

    print(f"Tool Result : {result}")

    # Delay to avoid rate limit
    print("\nWaiting 10 seconds...\n")
    time.sleep(10)

    # Continue Conversation
    messages = [
        types.Content(
            role="user",
            parts=[
                types.Part(text=user_query)
            ]
        ),

        response.candidates[0].content,

        types.Content(
            role="tool",
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

    final = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages
    )

    return final.text


# ---------------- Test ----------------
queries = [
    "What's the weather like in Chennai?",
    "Is it a good day to go out in Noida?",
    "Should I carry an umbrella in Mumbai today?"
]

for query in queries:
    print("=" * 50)
    print("User:", query)

    try:
        answer = ask_weather(query)
        print("Bot :", answer)

    except Exception as e:
        print("Error:", e)
        
'''

'''

# Multi Tools

from google import genai
from google.genai import types
import time

client = genai.Client()


def get_weather(city: str) -> dict:
    weather_data = {
        "Delhi": {"temp": 38, "condition": "Sunny"},
        "Mumbai": {"temp": 30, "condition": "Humid"},
        "Bangalore": {"temp": 24, "condition": "Cloudy"},
        "Chennai": {"temp": 34, "condition": "Rainy"},
        "Noida": {"temp": 36, "condition": "Hazy"}
    }

    return weather_data.get(city, {"temp": 0, "condition": "Unknown"})


def calculate(expression: str) -> dict:
    try:
        result = eval(expression)
        return {
            "expression": expression,
            "result": result
        }

    except Exception as e:
        return {"error": str(e)}


def search_docs(query: str) -> dict:
    docs = {
        "python": "Python is a high-level programming language.",
        "rag": "RAG stands for Retrieval Augmented Generation.",
        "agent": "An AI Agent can reason and use tools autonomously."
    }

    for key, value in docs.items():
        if key in query.lower():
            return {
                "found": True,
                "content": value
            }

    return {
        "found": False,
        "content": "No result found."
    }


tools = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="get_weather",
            description="Get current weather for a city",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "city": types.Schema(
                        type=types.Type.STRING,
                        description="City name"
                    )
                },
                required=["city"]
            )
        ),

        types.FunctionDeclaration(
            name="calculate",
            description="Evaluate a mathematical expression",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "expression": types.Schema(
                        type=types.Type.STRING,
                        description="Math expression to evaluate"
                    )
                },
                required=["expression"]
            )
        ),

        types.FunctionDeclaration(
            name="search_docs",
            description="Search documentation for a topic",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "query": types.Schema(
                        type=types.Type.STRING,
                        description="Topic to search"
                    )
                },
                required=["query"]
            )
        )
    ]
)


def execute_tool(name: str, args: dict) -> dict:

    if name == "get_weather":
        return get_weather(**args)

    elif name == "calculate":
        return calculate(**args)

    elif name == "search_docs":
        return search_docs(**args)

    return {"error": "Unknown tool"}


def run_agent(user_query: str):

    messages = [
        types.Content(
            role="user",
            parts=[
                types.Part(text=user_query)
            ]
        )
    ]

    time.sleep(60)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[tools]
        )
    )

    part = response.candidates[0].content.parts[0]

    if part.function_call:

        fn_name = part.function_call.name
        fn_args = dict(part.function_call.args)

        result = execute_tool(fn_name, fn_args)

        messages.append(response.candidates[0].content)

        messages.append(
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
        )

        time.sleep(60)

        final = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[tools]
            )
        )

        return final.text

    return part.text


queries = [
    "What is the weather in Mumbai?",
    "What is 1847 multiplied by 23?",
    "What is RAG in AI?"
]


for query in queries:
    print(f"\nUser: {query}")
    print(f"Bot: {run_agent(query)}")
    print("-" * 50)
    time.sleep(60)
'''

'''

# streaming response

from google import genai
from google.genai import types

client = genai.Client()

# generate_content_stream instead of generate_content
for chunk in client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents="Explain how the internet works in detail."
):
    print(chunk.text, end="", flush=True)

print() 
'''

'''

# Streaming with system prompt

from google import genai
from google.genai import types

client = genai.Client()

def stream_response(user_input: str):
    print("Bot: ", end="", flush=True)

    for chunk in client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction="You are a concise AI tutor. "
                               "Always answer in bullet points."
        )
    ):
        print(chunk.text, end="", flush=True)

    print()  # newline at end


# Test
stream_response("What are the phases of the moon?")
'''

# Streaming with history

from google import genai
from google.genai import types

client = genai.Client()

def stream_and_collect(user_input: str) -> str:
    full_response = ""

    print("Bot: ", end="", flush=True)

    for chunk in client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful assistant. do not give long answers. explain in points"
        )
    ):
        print(chunk.text, end="", flush=True)
        full_response += chunk.text 

    print()

    characters_full_response = len(full_response)

    tokens = characters_full_response // 4

    print("-"* 50)

    print(f"Tokens (approx): {tokens}")
    print(f"Characters: {characters_full_response}")

    print("-" * 50)

    return full_response , characters_full_response , tokens



reply = stream_and_collect("Explain the difference between supervised and unsupervised learning.")

