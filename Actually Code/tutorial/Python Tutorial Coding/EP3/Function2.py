# Write a program that defines a function called max_number that
# takes a list of numbers and returns the maximum number in the list.
# The program should test the function by calling it with a few different
# lists of numbers.
import random
lst1 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = []
lst3 = []


def max_number(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number >= max_num:
            max_num = number
    return max_num


def append_aleatory_numbers(numbers):
    for i in range(11):
        numbers.append(random.randint(0, 100))


append_aleatory_numbers(lst2)
append_aleatory_numbers(lst3)

print(max_number(lst1))
print(max_number(lst2))
print(max_number(lst3))
