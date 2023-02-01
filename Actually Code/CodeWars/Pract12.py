"""Complete the function/method (depending on the language) to return true/True
when its argument is an array that has the same nesting structures and same
corresponding length of nested arrays as the first array.
"""


def calculate_len(argument: list):
    equals_original = []
    for element in argument:
        if isinstance(element, int):
            equals_original.append(-1)
        elif isinstance(element, list):
            if all(isinstance(item, list) for item in element):
                equals_original.append(None)
            else:
                equals_original.append(len(element))
    return equals_original


