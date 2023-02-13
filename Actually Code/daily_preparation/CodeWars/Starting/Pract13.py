"""In this kata, your task is to create all permutations of a non-empty
input string and remove duplicates, if present.

Create as many "shufflings" as you can!
"""

from itertools import permutations as per

def permutations(s):
    s = list(s)
    return list(set(["".join(p) for p in per(s)]))


print(permutations('a'))  # , ['a']);
print(permutations('ab'))  # , ['ab', 'ba'])
# , ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
print(permutations('aabb'))
