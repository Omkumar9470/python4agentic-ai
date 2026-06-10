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



