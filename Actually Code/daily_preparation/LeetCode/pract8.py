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
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    # def mergeTwoLists(self, list1: list[int], list2: list[int]) -> list:
    #     result = []
    #     for element in list([x1]+[x2] for x1, x2 in zip(sorted(list1), sorted(list2))):
    #         for integral in element:
    #             result.append(integral)
    #     if (len(list1) + len(list2))!=len(result):
    #         if list1:
    #             for element in list1:
    #                 if element not in result:
    #                     result.append(element)
    #         if list2:
    #             for element in list2:
    #                 if element not in result:
    #                     result.append(element)
    #     return result


print(Solution().mergeTwoLists([4,2,1], [4,3,1]))
print(Solution().mergeTwoLists([1, 2, 4], [1, 3, 4]))
print(Solution().mergeTwoLists([1, 2, 4], [1]))
print(Solution().mergeTwoLists([1], [1, 3, 4]))
print(Solution().mergeTwoLists([], []))
print(Solution().mergeTwoLists([], [0]))
print(Solution().mergeTwoLists([0],[]))
