"""The task is to write a function is_interesting(number, awesome_phrases)
that returns 0, 1, or 2 based on whether the input number is an "interesting" number or not.

An "interesting" number is a 3-or-more digit number that meets one of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incrementing: 1234
The digits are sequential, decrementing: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases list
If an "interesting" number is within two miles of the input number, 
the function should return 1. If the input number is itself an "interesting"
number, the function should return 2. If neither of these criteria are met,
the function should return 0.

The input number will always be an integer greater than 0 and less than 
1,000,000,000. The awesome_phrases list will always be provided, and may be empty.
"""


def main_process(number: int) -> bool:
    string_number = str(number)
    if is_palindrome_or_equal(string_number):
        return True
    elif number_is_round(string_number):
        return True
    elif is_consecutive(string_number):
        return True
    return False


def is_palindrome_or_equal(string_number: str) -> bool:
    if string_number == string_number[::-1]:
        return True
    return len(set(string_number)) == 1


def number_is_round(string_number: str) -> bool:
    return string_number.count("0") == (len(string_number)-1)


def is_consecutive(string_number: str) -> bool:
    digits = tuple(int(x) for x in string_number)

    def check_consecutive(digits: tuple) -> bool:
        counter = 0
        # hard_check = ""
        for i, num in enumerate(digits):
            if digits[i] != digits[-1] and num != 9:
                if (num + 1) == digits[i + 1]:
                    counter += 1
                    # hard_check += str(num)
                else:
                    # hard_check = ""
                    counter = 0
            elif digits[i] != digits[-1] and num == 9:
                if digits[i + 1] == 0:
                    counter += 1
                    # hard_check += str(num)
                else:
                    counter = 0
                    # hard_check = ""
            else:
                if num == digits[i - 1] + 1:
                    counter += 1
                    # hard_check += str(num)
                break
            if counter >= 3:
                break
        # if hard_check == "901":
        #     print(1)
        #     raise SystemExit
        return counter >= 3

    if check_consecutive(digits):
        return True
    return check_consecutive(digits[::-1])


def close_to_be_interesting(number: int) -> bool:
    numbers = set([number - x for x in range(1, 3)] +
                  [number + x for x in range(1, 3)])
    for item in numbers:
        if main_process(item):
            return True
    return False


def math_check(original_num: int, awesome_number: int) -> bool:
    result = abs(original_num - awesome_number)
    return result >= 1 and result <= 2

