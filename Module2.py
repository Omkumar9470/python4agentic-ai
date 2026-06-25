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