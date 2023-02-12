"""Valid Parentheses
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, string: str) -> bool:
        length_string = len(string)
        if length_string <= 1:
            return False
        for i in range(len(string)):
            if i == length_string:
                break
            parenthesis_1 = ord(string[i])
            parenthesis_2 = ord(string[i+1])
            if parenthesis_1 == 40:
                if parenthesis_2 == 41:
                    continue
            elif parenthesis_1 == 91:
                if parenthesis_2 == 93:
                    continue
            elif parenthesis_1 == 123:
                if parenthesis_2 == 126:
                    continue
            else:
                return False

        return True


print(Solution().isValid("()"))  # True
print("------------------------------------")
print(Solution().isValid("()[]{}"))  # False
print("------------------------------------")
print(Solution().isValid("(]"))  # false
