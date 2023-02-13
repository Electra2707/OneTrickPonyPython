"""Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: list[int], list2: list[int]) -> list:
        result = []
        for element in list([x1]+[x2] for x1, x2 in zip(list1, list2)):
            for integral in element:
                result.append(integral)
        if (len(list1) - len(list2)) <= -1:
            if len(list2) == 1:
                result = list2
            else:
                result.append(list1[(len(list1) - len(list2))])
        if (len(list2) - len(list1)) <= -1:
            if len(list1) == 1:
                result = list1
            else:
                result.append(list2[(len(list2) - len(list1))])
        return result


print(Solution().mergeTwoLists([1, 2, 4], [1, 3, 4]))
print(Solution().mergeTwoLists([1, 2, 4], [1]))
print(Solution().mergeTwoLists([1], [1, 3, 4]))
print(Solution().mergeTwoLists([], []))
print(Solution().mergeTwoLists([], [0]))
print(Solution().mergeTwoLists([0],[]))
