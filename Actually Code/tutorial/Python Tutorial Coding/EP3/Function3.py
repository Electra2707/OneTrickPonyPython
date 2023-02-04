# Write a program that defines a function called is_palindrome that takes a string and returns True
# if the string is a palindrome (i.e. reads the same forwards and backwards), and False otherwise.
# The program should test the function by calling it with a fe
import time

def ask_word():
    while True:
        word = input("Write your word: ")
        if not word or not word.strip():
            print("Invalid input try again")
        else:
            return word
            break


def is_palindrome(str):
    palindrome = str[::-1]
    if str == palindrome:
        return True
    else:
        return False


word = ask_word()
case_sensitivity = word.lower()
if is_palindrome(case_sensitivity):
    print(f"The word {word} is a palindrome")
else:
    print(f"The word {word} isn't a palindrome")

time.sleep(5)