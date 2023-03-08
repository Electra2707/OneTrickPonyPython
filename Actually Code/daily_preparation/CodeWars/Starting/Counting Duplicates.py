"""Counting Duplicates
Write a function that will return the count of distinct case-insensitive
alphabetic characters and numeric digits that occur more than once in the
input string. The input string can be assumed to contain only alphabets
(both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""


def duplicate_count(text: str):
    if not text:
        return 0
    text = text.casefold()
    counter = 0
    seen = set()
    for i in text:
        if i in seen:
            continue
        num = text.count(i)
        if num >= 2:
            counter += 1
            seen.add(i)
    return counter


print(duplicate_count(""))
print(duplicate_count("abcde"))
print(duplicate_count("abcdeaa"))
print(duplicate_count("abcdeaB"))
print(duplicate_count("Indivisibilities"))
