"""Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""


class Solution:
    def checkInclusion(self, find_permutations: str, letters: str) -> bool:
        items_in_letter = [x for x in letters]
        for i, char in enumerate(items_in_letter):
            items_in_letter.count()


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidboaoo"
    # s1=input()
    # s2=input()
    print(Solution().checkInclusion(s1, s2))
