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

'''

#Skill Manager

skills = []

while True:
    print("Skill manager \n")

    print("1. Add Skill \n")
    print("2. Remove Skill \n")
    print("3. Show Skill \n")
    print("4. Exit")
    print("Enter Your Choice (1,2,3,4)")
    choice = int(input(" "))

    if choice == 1:
        print("Add Your Skill \n")
        skill = input(" ")


        skills.append(skill)
        print("Skill added successfully \n")
    
    elif choice == 2:
        print("Enter the skill you want to remove \n")
        skill = input(" ")

        skills.remove(skill)

        print("Skill Removed Successfully \n")
    
    elif choice == 3:
        print("Your Skills Are---")

        for skill in skills:
            print(skill)

    elif choice == 4:
        print("Exiting")
        break

    else:
        print("Invalid Choice Retry")
        continue
'''

'''
#Duplicate Remover

nums = set()

while True:
    print("Your Favourite number")
    print("1. Add number")
    print("2. Show")
    print("3. Exit")

    choice = int(input("Choose 1,2 or 3 ---"))

    if choice == 1:
        print("Enter Your Number \n")
        num = int(input(" "))

        nums.add(num)
        print("Number added successfully")
    
    elif choice == 2:
        print("Your Numbers Are --")
        print(nums)
    
    elif choice == 3:
        break

    else:
        print("Wrong Choice, Enter a Valid Choice")
        continue
'''

'''

#Student Management

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def show_details(self):
        print(f"Student Report -> Name: {self.name} | Age: {self.age} | marks: {self.marks}")


student_list = []

while True:
    print("\n ---Student Management System--- \n")
    print("\n 1. Add New Student")
    print("\n 2. Show All Students")
    print("\n 3. Exit")

    choice = int(input("\n Enter your choice 1,2 or 3 : \n  "))

    if choice == 1:
        print("\n Enter Details of the New student")
        name = input("\n Enter Name Of The Student:  ")
        age = int(input("Enter The Age OF The Student:  "))
        marks = int(input("Enter The Marks Obtained By The Student:  "))

        new_student = Student(name, age, marks)

        student_list.append(new_student)

        print(f"Student is added successfully for {name}")
    
    elif choice == 2:
        print("Here is the list of the students")

        for student in student_list:
            student.show_details()

    elif choice == 3:
        break

    else:
        print("Invalid choice, Retry")
        continue
'''

'''
# BankAccount

class BankAccount:
    def __init__ (self, initial_balance):
        self.balance = initial_balance
    
    def deposit (self, deposit_amount):
        self.balance += deposit_amount
        print(f"Deposited : {deposit_amount} rupees")

    def withdraw (self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print(f"Withdrawed : {withdraw_amount} rupees")

        else:
            print("insufficent Balnace Try Again")

    def checkbalance(self):
        print(f"You Balance is {self.balance}")

account1= BankAccount(100)



while True:
    print("Press 1 to doposit in your account")
    print("Press 2 for withdraw")
    print("Press 3 to check balance")
    print("Press 4 to exit")

    choice = int(input())
    if choice == 1:
        print("Enter The amount To Deposite \n")
        amount = int(input("-> "))
        account1.deposit(amount)
    
    elif choice == 2:
        print("Enter The Amount For Withdrawl \n")
        amount = int(input("-> "))
        account1.withdraw(amount)

    elif choice == 3:
        account1.checkbalance()
    
    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Wrong input Try Again")
        continue
'''

'''

# AI Agent

class Agent:
    def __init__ (self):
        self.memory = []

    def think (self, user_input):
        print(f"Thinking about: '{user_input}' ")
    
    def act (self, user_input):
        print(f"Acting On : '{user_input}' ")
    
    def remember (self, user_input):
        print(f"I will remember : '{user_input}' ")
        self.memory.append(user_input)

agent1 = Agent()

while True:
    print("listening")
    text = input("---")

    if text.lower() == 'quit':
        break


    agent1.think(text)
    agent1.act(text)
    agent1.remember(text)

'''    

'''
# Employee System

class Employee :
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def show_details (self):
        print(f"Name: {self.name} | Age: {self.age} ")

class Developer(Employee):
    def __init__(self, name, age, programming_lang):
        super().__init__(name, age)

        self.programming_lang = programming_lang
    
    def show_details (self):
        print(f"Role : Developer | Programing Language : {self.programming_lang}")

class Manager(Employee):
    def __init__ (self, name, age, team_size):
        super().__init__(name, age)

        self.team_size = team_size
    
    def show_details(self):
        print(f"Role : Manager | Team Size : {self.team_size}")

dev1 = Developer("Om", 23, "Python")
mang1 = Manager("laudi", 21, "11")

dev1.show_details()
mang1.show_details()

'''

'''
# Notes App

def add_note(text):
    with open("notes.txt", "a") as file:
        file.write(F"\n {text}")
    
    print("Note added successfully")

def show_note():
    with open("notes.txt", "r") as file:
        for line in file:
            print(line)

print("Welcome To the Notes App")

while True:
    print("Press 1 to write in your notes")
    print("Press 2 to view all the notes")
    print("press 3 to exit")

    choice = int(input("-> "))

    if choice == 1:
        print("Write your Note here")

        text = input(" ")

        add_note(text)
    
    elif choice == 2:
        show_note()
    
    elif choice == 3:
        print("Thanks Your Using")
        exit()
    
    else:
        print("Wrong Choice Try Again.")
'''

'''

# Student JSON Database
import json

user = {
  "name": "Om",
  "age": 22,
  "skills": ["Python", "AI"]
}

json_data = json.dumps(user)

print(json_data)

'''

'''
# Chat History Saver

def chat_saver(user_response):
    with open("notes.txt", "a") as file:
        file.write(f"\n User_Response: {user_response}")
        print("Response Saved...")

while True:
    print("What Do You Want To Say? or type exit to close the program.")
    user_response = input(" ")
    if user_response.lower() == 'exit':
        print("Agent Stopped")
        break
    else:
        chat_saver(user_response)

'''

'''

# User Profile Manager


import json

def save_json(profile):
    # 1. Read the existing list from the file
    with open("temp.json", "r") as file:
        database = json.load(file)  # This reads the list []
    
    # 2. Append your new user dictionary into that list
    database.append(profile)
    
    # 3. Overwrite the file ("w") with the completely updated list
    with open("temp.json", "w") as file:
        json.dump(database, file, indent=4)

    print("User added successfully")

def read_json():
    with open("temp.json", "r") as file:
        data = json.load(file)
        
        print("\n--- Current Users ---")
        # Since data is now a proper list, loop through it to display it cleanly
        for u in data:
            print(f"Name: {u['name']} | Age: {u['age']}")
        print("---------------------\n")


# Fixed: Moved this inside the loop so old data clears out for new entries
# user = {} 

while True:
    print("To add user press 1")
    print("To view users press 2")
    print("To exit press 3")

    choice = int(input("-> "))

    if choice == 1:
        print("Enter Details")

        # Fixed: Creating a clean dictionary for each individual entry
        user = {} 
        
        print("Enter Your Name:")
        a = input("---")
        user["name"] = a
        print("Enter your Age:")
        b = int(input("---"))
        user["age"] = b

        save_json(user)

    elif choice == 2:
        read_json()

    elif choice == 3:
        print("quiting")
        break

    else :
        print("Wrong input")
'''

'''

# Chat History Saver


def file_write (user_response):
    with open("notes.txt", "a")as file:
        file.write(f"{user_response}\n")

while True:
    print("What Do You Want To Say? (Type 'exit' to end chatting)")
    user_response = input("")
    if user_response.lower() == 'exit':
        print("Thanks For The Chat, We have saved your data")
        break
    
    file_write(user_response)
    print(f"Got it you said '{user_response}' ")
'''


'''
# User Profile Manager

import json

def save_user (profile):
    
    with open("temp.json", "r") as file:
        database = json.load(file)

    database.append(profile)

    with open("temp.json", "w") as file:
        json.dump(database, file, indent=4)
    
    print("User added successfully")

def read_json ():

    with open("temp.json", "r") as file:
        data = json.load(file)

        print("current users")

        for u in data:
            print(f"Name:{u['name']} | Age: {u['age']}")
        

while True:
    print("1 To add new user")
    print("2 for see all users")
    print("3 for exit")

    response = input("")

    if response == 1:
        print("Give user details")

        user = {}

        print("Enter name")
        name = input("")
        user["name"] = name
        print("Enter age")
        age = int(input(""))
        user["age"] = age

        save_user(user)
    
    elif response == 2:
        read_json()

    elif response == 3:
        print("Thanks for using the user database")
        break

    else:
        print("unexpted error")
        continue
'''

'''
# Safe Calculator

def add (a,b):
    print(f"Result: {a + b}")

def subtract(a,b):
    print( f"Result: {a-b}")

def multiply(a,b):
    print( f"Result: {a*b}")

def divide(a,b):
    if b == 0:
        print("Error: Cannot Divide By Zero")
    else:
        print (f"Result: {a/b}")

while True:
    print("Enter Two Numbers")
    try:
        a = int(input("Enter the first number ->  "))
    except ValueError:
        print("Error: Enter a Valid number")
        continue

    try:
        b = int(input("Enter the second number ->  "))
    except ValueError:
        print("Error: Enter a Valid number")
        continue

    print("Select Operation")
    print("Press 1 for addition ")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")    
    print("Press 5 to exit")

    try:
        choice = int(input(" "))
    except ValueError:
        print("Please select numbers")
    
    if choice==1:
        add(a,b)
    elif choice == 2:
        subtract(a,b)
    elif choice == 3:
        multiply(a,b)
    elif choice==4:
        divide(a,b)

    elif choice==5:
        print("Thanks for using ther calculator")
        break
    
    else:
        print("Choice between 1 to 5")
'''

'''

# ATM System

def checkbalance(balance):
    print(f"Your Account Balance: {balance}")

def withdraw(balance, amount):

    if amount > balance:
        print("Insufficent Balance")
    
    else:
        new_balance = balance - amount
        print(f"Withdrawal successful. Remaining cash in account: {new_balance}")
        return new_balance

balance = 0
while True:
    print("Choose Your Transection")
    print("Press 1 for balance enquery")
    print("Press 2 for deposit")
    print("Press 3 for withdraw")
    print("To exit press 4")

    choice = int(input("-> "))

    if choice == 1:
        checkbalance(balance)
    elif choice == 2:
        print("Enter the amount to deposit")
        
        try:
            amount = int(input("-> "))
        except ValueError:
            print("Please Enter A Valid Amount")
            continue

        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            continue

        balance += amount
        print("Deposite successfull")
        print(f"Your Updated Balance : {balance}")
    
    elif choice == 3:
        print("Enter The Amount For Withdrawl")

        try:
            amount = int(input("-> "))
        except ValueError:
            print("Please Enter A Valid Amount")
            continue

        if amount <= 0:
            print("Error: Withdrawl amount must be greater than zero.")
            continue

        balance = withdraw(balance, amount)

    elif choice == 4:
        print("Thanks For Using ATM")
        break
    else:
        print("Enter A valid choice")
        continue

'''

'''

# File Reader

def open_file(filename):
    try:
        with open (filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found")

while True:
    print("Enter the file name to read it.")
    print("To exit type 'quit' ")
    filename = input("")

    if filename.lower() == 'quit':
        print("Exiting.............")
        break
    
    open_file(filename)
'''


'''

# Login Validator

class UsernameTooShortError(Exception):
    pass

class WeakPasswordError(Exception):
    pass


def username_validator(username):
    
    if len(username) <= 5:
        raise UsernameTooShortError("Username must be greater than 5 characters.")

    print("Username Accepted")
    return username

def pass_validator(password):
    
    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters long.")
    
    has_digit = False
    has_upper = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    
    if not has_digit:
        raise WeakPasswordError("Password must contain at least one digit (0-9).")

    if not has_upper:
        raise WeakPasswordError("Password must contain at least one uppercase letter (A-Z).")
    
    print("Password Accepted")
    return True

while True:
    print("\n--- Account Registration Validator ---")

    try:
        username = input("Enter Your Username -> ")
        password = input("Enter Your Password -> ")

        username_validator(username)

        pass_validator(password)

        break

    except UsernameTooShortError as error_message:
        print(f"\n Failed: {error_message}")
        print("Please try again.")
    
    except WeakPasswordError as error_message:
        print(f"\n Failed: {error_message}")
        print("Please try again.")
'''

# Student Marks Analyser

while True:
    print("Enter the marks for all 7 subjects (out of 100).")

    marks= []
    subject_counter = 1

    while subject_counter <= 7:
        try:
            m1 = int(input(f"Subject {subject_counter} -> "))
            if m1 < 0 or m1 > 100:
                print("Error: Marks must be between 0 and 100.")
                continue
            marks.append(m1)
            subject_counter += 1
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")
            continue

    print(f"Marks obtained by the student are {marks}")

    passed_subjects = list(filter(lambda score: score >= 35, marks))
    failed_subjects = list(filter(lambda score: score < 35, marks))

    top_scores = list(filter(lambda score: score >= 90, marks))

    print("Here is the report")
    print("-" * 50)
    print(f"Passed Subjects ->  {passed_subjects}")
    print(f"Failed Subjects ->  {failed_subjects}")
    print(f"Top Scores ->  {top_scores}")
    print("-"*50)
    print("School Allow Some Grace Marks ")

    saved_students = list(
        map(lambda score: score + 5, filter(lambda score: score < 40, marks)))
    
    print("-"*50)
    print(f"Originally Failed Students after +5 Grace Boost: {saved_students}")

    exit_choice = input("\nAnalyze another student? (y/n): ")
    if exit_choice.lower() != 'y':
        print("Closing Analyser System. Goodbye.")
        break

    

