#Use list comprehension in this code

def flatten(lst):
    flattened = []
    for sublist in lst:
        for item in sublist:
            flattened.append(item)
    return flattened

example_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = flatten(example_list)


def flatten(lst):
    return [item for sublist in lst for item in sublist]

example_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = flatten(example_list)