from Basic import ask_num
import random
import string

def ask_num():
    print("Write your integral number")
    while True:
        try:
            num1=input()
            if not num1.isnumeric() or not num1.strip():
                print("Invalid input, try again")
            else:
                return int(num1)
                break
        except ValueError:
            print("Invalid input try again")

# def generate_random_password(numbers):
#     generate1=[]
#     [generate1 for number in numbers]
#     alt = random(1, 100)
#     word = ""
#     word_a = word.replace(alt, string.printable)
#     generate1.append(word_a)
#     return generate1

def generate_random_password(numbers):
    password = ""
    for i in range(numbers):
        alt=random.randint(0,len(string.printable)-1)
        password += string.printable[alt]
    return password


    # return [number for number in int for number in 5random(1,100) ]
print("This program will generate a random password in base of the lenth of one input number")
numbers = ask_num()
password = generate_random_password(numbers)
password = str(password)

print(password)
