"""Remove Element
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the 
first two elements of nums being 2.
It does not matter what you leave beyond the returned k 
(hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the 
first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k 
(hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""
from typing import List


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         if not nums:
#             return 0
#         for i, element in enumerate(nums):
#             if element == val:
#                 nums.pop(i)
#         if val in nums:
#             Solution().removeElement(nums, val)
#         return len(nums)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                i -= 1  # go back one step
            i += 1  # increment i
        return len(nums)


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         if not nums:
#             return 0
#         i = 0  # pointer for scanning
#         j = 0  # pointer for placing
#         while i < len(nums):
#             if nums[i] != val:
#                 # copy non-matching element to next position
#                 nums[j] = nums[i]
#                 j += 1  # increment j
#             i += 1  # increment i
#         return j  # return number of non-matching elements


print(Solution().removeElement([3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3,
      3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1], 3))
