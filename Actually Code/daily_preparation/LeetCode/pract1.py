"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i,num in enumerate(nums):
#             for j,num1 in enumerate(nums):
#                 if num1 + num == target:
#                     return [i,j]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complement_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_map:
                return [complement_map[complement], i]
            complement_map[num] = i
        return []
    
print(Solution().twoSum([2,7,11,15],9))