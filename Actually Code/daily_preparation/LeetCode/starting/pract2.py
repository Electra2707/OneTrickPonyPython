"""Given an integer x, return true if x is a 
palindrome
, and false otherwise.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_number=str(x)
        if string_number == string_number[::-1]:
            return True
        else:
            return False