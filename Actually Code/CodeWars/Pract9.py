"""Find the missing letter
Write a method that takes an array of consecutive (increasing)
letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly 
one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!
"""


def find_missing_letter(chars: list[str]) -> str:
    upper_case = chars[0].isupper()
    if upper_case:
        chars = [char.lower() for char in chars]
    alphabet = {i+1: chr(i+97) for i in range(26)}
    first_letter = ord(chars[0]) - ord('a') + 1
    last_letter = ord(chars[-1]) - ord('a') + 1
    missing_char = [alphabet[i] for i in range(
        first_letter, last_letter+1) if alphabet[i] not in chars]
    return missing_char[0].upper() if upper_case else missing_char[0]


def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))


def find_missing_letter(c):
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))  # , 'e')
print(find_missing_letter(['O', 'Q', 'R', 'S']))  # , 'P')
