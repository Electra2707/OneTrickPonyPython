import random
num1=random.randint(1,10)
print("Guess what number I'm thiking of in 1-10")

try:
    choice=int(input())
    if choice == num1:
        print("You guessed correctly!")
    elif choice>10:
        print("You write a number bigger than 10")
    elif choice<1:
        print("You write a number less than 1")
    else:
        print(f"Sorry, the correct answer was {num1} while you answer was {choice}")
except ValueError:
    print("You didn't even try to input a number...")