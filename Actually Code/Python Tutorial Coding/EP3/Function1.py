# Write a program that defines a function called sum_numbers that takes a list of numbers and
# returns the sum of the numbers. The program should test the function by calling it with a few
# different lists of numbers.

from Basic import ask_num
import os

print("Create your list")
lst = []
while True:
    n = ask_num()
    lst.append(n)
    print("Do you want to add more numbers? S/N")
    continue1 = input()
    continue1 = continue1.upper()
    if continue1 == "N":
        os.system("cls")
        break
    else:
        pass

def sum_numbers(lst):
    total_numbers = sum(lst)
    return total_numbers

result = sum_numbers(lst)
print(f"The sum of all of the numbers in the list is {result}")

