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