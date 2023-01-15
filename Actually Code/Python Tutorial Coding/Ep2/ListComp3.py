# Use list comprehension in this code

# def double_numbers(lst):
#     doubled = []
#     for number in lst:
#         doubled.append(number * 2)
#     return doubled

# def double_numbers(lst):
#     return [doubled for number in lst (number*2)]

def double_numbers(lst):
    return [number * 2 for number in lst]

example_list = [1, 2, 3, 4, 5]
doubled = double_numbers(example_list)
