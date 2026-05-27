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

