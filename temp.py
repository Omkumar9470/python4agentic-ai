'''
num = int(input("Enter a number: "))

count = 1

while count <= 10:
    print(num,"*",count,"=",num*count)
    count += 1
'''

'''
import random

fixed_num = random.randint(0,5)

n = ""

while n!= fixed_num:
    print("Guess the Number")
    n = int(input())
    
    if n == fixed_num :
        print("Nice guess, The number is -",n)
        break
    else :
        print("You guesses Wrong")
        continue
'''

'''
while True:
    print("Hello mate what you want to say !")
    text = str(input())
    if text == 'exit' :
        break
    else:
        print("oh you said-",text)
        continue
'''

'''
passw = "hey_bb"

enter_passw = ""
i = 0

for i in range (3):
    print("Enter the password")
    enter_passw = str(input())
    if enter_passw == passw :
        print("Login success")
        break
    else:
        print("Wrong password")
        continue
'''
'''
#Calculator Using Functions
def add (a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

a = int(input("Enter the first number"))
b= int (input("Enter the second number"))
print("Select the opertaion Add, Subtract, Multiply, Divide")
choice = int(input("Choose 1,2,3,4"))

if choice==1:
    print(add(a,b))

elif choice==2:
    print(subtract(a,b))

elif choice == 3:
    print(multiply(a,b))

elif choice == 4:
    print(divide(a,b))

else:
    print("Unexpected Error, choose between 1 - 4")
'''

'''
#AI Chatbot Structure

def get_input():
    user_input = input("What DO You Want To Say: ")
    return user_input

user_input_final = get_input()

def generate_response(user_input_final):
    if user_input_final == "Hello":
        return "Hi, nice to meet you"
    
    else:
        return "Ok I heard you, you said -", user_input_final
response_final= generate_response(user_input_final)

def display_response(response_final):
    print(response_final)

display_response(response_final)

'''

'''
# Temperature Converter

def celsius_to_fahrenheit(temp):
    return (temp * (9/5)) + 32

def fahrenheit_to_celsius(temp):
    return (temp-32)*(5/9)

print("What You want to convert choose")
print("1 for celsius_to_fahrenheit")
print("2 for fahrenheit_to_celsius")
choice = int(input(" "))
temp = float(input("Enter the Tempurature: "))

if choice==1:
    print(celsius_to_fahrenheit(temp))

elif choice==2:
    print(fahrenheit_to_celsius(temp))

else:
    print("Enter a valid response")

'''


'''
#Student Database

student_db = {
    
}


print("Enter Your Name:")
a = input("---")
student_db["name"] = a
print("Enter your Age:")
b = int(input("---"))
student_db["age"] = b
print("Enter Your Marks:")
c = int(input("---"))
student_db["marks"] = c

print(student_db)
'''


'''
#Contact Book

contact = [
    {
        "name": "Om",
        "number": 123
    },
    {
        "name": "Jay",
        "number": 142
    }
]

while True:
    print("\n--- Contact Book---")
    print("1. View all Contacts")
    print("2. Add New Contact")
    print("3. Exit")

    choice = int(input("\n---Enter Your Choice--\n"))

    if choice == 1:
        print("\n Your contacts are.")
        for person in contact:
            print(f"Name:", person["name"], "Phone:", person["number"])
    
    elif choice == 2:
        print("\n Add a New Contact \n")
        new_name = input("Enter Name: ")
        new_number = int(input("Enter Number: "))

        new_entry = {"name": new_name, "number": new_number}

        contact.append(new_entry)
        print("Contact added successfully")

    elif choice== 3:
        print("Exited Successfully")
        break

    else:
        print("Enter a valid choice")
        continue

'''