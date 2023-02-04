def flatten_and_filter(lst):
    flattened = []
    for sublist in lst:
        for item in sublist:
            if item % 2 == 0:
                flattened.append(item)
    return flattened


example_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_evens = flatten_and_filter(example_list)


def flatten_and_filer(lst):
    return [item for sublist in lst for item in sublist if item % 2 == 0]
