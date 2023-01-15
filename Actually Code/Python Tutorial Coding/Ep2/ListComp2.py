# Use list comprehension in this code

def even_numbers(lst):
    evens = []
    for number in lst:
        if number % 2 == 0:
            evens.append(number)
    return evens


example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = even_numbers(example_list)


def even_numbers(lst):
    return [evens for number in lst if number % 2 == 0]


example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = even_numbers(example_list)
