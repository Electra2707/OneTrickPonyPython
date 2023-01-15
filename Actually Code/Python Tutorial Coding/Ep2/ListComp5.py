def double_and_filter(lst):
    doubled = []
    for number in lst:
        result = number * 2
        if result % 2 == 1:
            doubled.append(result)
    return doubled


example_list = [1, 2, 3, 4, 5]
doubled_odds = double_and_filter(example_list)


def double_and_filter(lst):
    return [number * 2 for number in lst if (number*2) % 2 == 0]
