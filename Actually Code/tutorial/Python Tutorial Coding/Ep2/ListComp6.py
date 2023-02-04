def flatten_double_and_filter(lst):
    flattened = []
    for sublist in lst:
        for item in sublist:
            flattened.append(item)
    doubled = []
    for number in flattened:
        result = number * 2
        if result % 2 == 0:
            doubled.append(result)
    return doubled


example_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_doubled_evens = flatten_double_and_filter(example_list)


def flatten_double_and_filter(lst):
    return [number*2 for number in ([item for sublist in lst for item in sublist]) if (number*2) % 2 == 0]
