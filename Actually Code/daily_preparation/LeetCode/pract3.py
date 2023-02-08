"""Given two strings s and p, return an array of all the start indices of 
p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def findAnagrams(self, long_string: str, find_string: str) -> list[int]:
        counter = []
        find_length = len(find_string)
        try:
            for i in range(len(long_string)):
                anagram = long_string[:i] + long_string[:find_length]
                if find_string == anagram:
                    counter.append(i)
        except IndexError:
            pass
        return counter


s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))
