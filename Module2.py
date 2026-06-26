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
