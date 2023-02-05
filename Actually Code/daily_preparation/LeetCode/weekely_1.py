"""Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""


class Solution:
    def checkInclusion(self, find_permutations: str, letters: str) -> bool:
        if len(find_permutations)>len(letters):
            return False
        for i in find_permutations:
            number_letter = letters.count(i)
            number_permutations = find_permutations.count(i)
            if number_letter < number_permutations:
                return False
        else:
            return True


if __name__ == "__main__":
    s1=input()
    s2=input()
    print(Solution().checkInclusion(s1, s2))
