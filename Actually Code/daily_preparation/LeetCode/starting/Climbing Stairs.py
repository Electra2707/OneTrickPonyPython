"""Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n):
        n, prev, curr = n + 1, 0, 1
        for _ in range(2, n+1):
            prev, curr = curr, curr + prev
        return curr


# test the function with some examples
print(Solution().climbStairs(11))  # prints 55
print(Solution().climbStairs(6))  # prints 5
print(Solution().climbStairs(9999))  # prints 1134903170

# def climbStairs(self, n: int) -> int:
#     if n <= 3:
#         return n
#     num1 = Solution().Fib(n-1)
#     num2 = Solution().Fib(n-2)
#     return num1 + num2

# def Fib(self, target: int):
#     a, b = 0, 1
#     while a*b < target:
#         a, b = b, b+a

# print(Solution().climbStairs(2))
# print(Solution().climbStairs(5))
# print(Solution().climbStairs(10))
# print(Solution().climbStairs(15))
# print(Solution().climbStairs(20))
