# Write a program that defines a function called sort_list that takes a list of numbers and returns the list sorted in ascending order.
# The program should test the function by calling it with a few different lists of numbers.
import random
lst1 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = []
lst3 = []


def append_aleatory_numbers(numbers):
    for i in range(11):
        numbers.append(random.randint(0, 100))


def sort_list(lst):
    lst.sort()  # lst.sort(reverse=True)
    return lst
# def sort_list(lst):
#     sorted_lst = sorted(lst)
#     return sorted_lst


append_aleatory_numbers(lst2)
append_aleatory_numbers(lst3)

print(sort_list(lst1))
print(sort_list(lst2))
print(sort_list(lst3))
