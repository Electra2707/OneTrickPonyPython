"""Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:

0 <= x <= 231 - 1
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        elif x == 1:
            return 1
        prev = 0
        for i in range(1, x):
            if (i * i) <= x:
                prev = i
            else:
                break
        return prev


print(Solution().mySqrt(1), "1,1")
print(Solution().mySqrt(2), "2")
print(Solution().mySqrt(3), "3")
print(Solution().mySqrt(4), "4,2")
print(Solution().mySqrt(5), "5")
print(Solution().mySqrt(6), "6")
print(Solution().mySqrt(7), "7")
print(Solution().mySqrt(8), "8")
print(Solution().mySqrt(9), "9,3")
print(Solution().mySqrt(10), "10")
print(Solution().mySqrt(11), "11")
print(Solution().mySqrt(12), "12")
print(Solution().mySqrt(13), "13")
print(Solution().mySqrt(14), "14")
print(Solution().mySqrt(15), "15")
