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
        if len(string) <= 1:
            return False
        for i in range(len(string)):
            if i is None:
                break
            print(i)

print(Solution().isValid("()")) #True
print("------------------------------------")
print(Solution().isValid("()[]{}")) #False
print("------------------------------------")
print(Solution().isValid("(]")) #false