"""Plus One
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. The digits are 
ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits: return [1]
        digits = "".join(map(str, digits))
        digits = str(int(digits) + 1)
        return list(map(int, digits))


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         i = len(digits) - 1 # start from the last digit
#         while i >= 0:
#             if digits[i] < 9: # no carry over
#                 digits[i] += 1 # add one
#                 return digits # return the result
#             else: # carry over
#                 digits[i] = 0 # set the digit to zero
#                 i -= 1 # move to the next digit
#         # if we reach here, it means all digits are nine
#         return [1] + digits # add one at the front and return

print(Solution().plusOne([]))
