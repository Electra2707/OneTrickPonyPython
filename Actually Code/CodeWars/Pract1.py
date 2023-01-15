"""Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""
import timeit


def to_camel_case1(text: str) -> str:
    try:
        if text.strip() == "":
            return ""
        text = text.replace("-", "_").replace(" ", "_")
        words = text.split("_")
        if text[0].islower():
            word = text.title()
            word = word.replace(word[0], word[0].lower())
            word = word.replace("_", "")
            return word
        if text[0].isupper():
            word = text.title()
            word = word.replace("_", "")
            return word
    except IndexError as I:
        print("Error incorrect value", I)


def to_camel_case2(text: str) -> str:
    try:
        if text.strip() == "":
            return ""
        text = text.replace("-", "_").replace(" ", "_")
        words = text.split("_")
        for i in range(1, len(words)):
            words[i] = words[i].capitalize()
        if text[0].isupper():
            words[0] = words[0].capitalize()
        return "".join(words)
    except IndexError as I:
        print("Error incorrect value", I)


def to_camel_case3(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0] + ''.join([x.capitalize() for x in removed[1:]])


def to_camel_case4(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


example1 = "the-stealth-warrior"
example2 = "The_Stealth_Warrior"

elapsed_time11 = timeit.timeit(lambda: to_camel_case1(example1))
elapsed_time12 = timeit.timeit(lambda: to_camel_case1(example2))
print(repr(to_camel_case1), elapsed_time11)
print(repr(to_camel_case1), elapsed_time12)
print("\n")


elapsed_time21 = timeit.timeit(lambda: to_camel_case2(example1))
elapsed_time22 = timeit.timeit(lambda: to_camel_case2(example2))
print(repr(to_camel_case2), elapsed_time21)
print(repr(to_camel_case2), elapsed_time22)
print("\n")


elapsed_time31 = timeit.timeit(lambda: to_camel_case3(example1))
elapsed_time32 = timeit.timeit(lambda: to_camel_case3(example2))
print(repr(to_camel_case3), elapsed_time31)
print(repr(to_camel_case3), elapsed_time32)
print("\n")


elapsed_time41 = timeit.timeit(lambda: to_camel_case4(example1))
elapsed_time42 = timeit.timeit(lambda: to_camel_case4(example2))
print(repr(to_camel_case4), elapsed_time41)
print(repr(to_camel_case4), elapsed_time42)
