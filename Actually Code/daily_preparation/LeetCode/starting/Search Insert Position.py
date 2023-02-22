"""Search Insert Position
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
from typing import List


class Solution:
    def searchInsert(self, nums, target):
        # Use binary search to find the target or the insertion position
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                low = mid + 1  # Target is in the right half
            else:
                high = mid - 1  # Target is in the left half
        return low  # Target not found, return the insertion position


# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         elif target < nums[0]:
#             return 0
#         elif target > nums[-1]:
#             return nums.index(nums[-1])+1
#         for i, num in enumerate(nums):
#             if num > target:
#                 return i


print(Solution().searchInsert([1, 3, 5, 6], 2))
