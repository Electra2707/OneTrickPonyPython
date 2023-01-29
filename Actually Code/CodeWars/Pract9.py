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


def find_missing_letter(chars: list[str]) -> list:
    alphabet = {i+1: chr(i+97) for i in range(26)}
    first_letter = ord(chars[0]) - ord('a') + 1
    last_letter = ord(chars[-1]) - ord('a') + 1
    chars_difference = []
    if chars[0].lower():
        for i in range(first_letter, last_letter+1):
            chars_difference.append(alphabet[i])
    else:
        for i in range(first_letter, last_letter+1):
            chars_difference.append(alphabet(i))
    return list(set(chars) - set(chars_difference))

find_missing_letter(['a', 'b', 'c', 'd', 'f'])  # , 'e')
find_missing_letter(['O', 'Q', 'R', 'S'])  # , 'P')
