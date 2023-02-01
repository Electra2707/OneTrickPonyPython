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


def same_structure_as(original: list, other: list):
    try:
        assert isinstance(original, list)
        assert isinstance(other, list)
    except AssertionError:
        return False
    equals_other = calculate_len(original)
    equals_original = calculate_len(other)
    if equals_original == equals_other:
        return True
    return False


def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as(o1, o2):
                return False
        else:
            return True
    else:
        return not isinstance(original, list) and not isinstance(other, list)


def same_structure_as(a, b):
    return (False if not (isinstance(a, list) and isinstance(b, list)) or len(a) != len(b)
            else all(same_structure_as(c, d) for c, d in zip(a, b) if isinstance(c, list)))


# , [[[],[]]] not same as [[1,1]]: True should equal False
print(same_structure_as([[[], []]], [[1, 1]]))
# , True, "[1,[1,1]] same as [2,[2,2]]")
print(same_structure_as([1, [1, 1]], [2, [2, 2]]))
