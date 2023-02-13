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


print(Solution().mergeTwoLists([4,2,1], [4,3,1]))
print(Solution().mergeTwoLists([1, 2, 4], [1, 3, 4]))
print(Solution().mergeTwoLists([1, 2, 4], [1]))
print(Solution().mergeTwoLists([1], [1, 3, 4]))
print(Solution().mergeTwoLists([], []))
print(Solution().mergeTwoLists([], [0]))
print(Solution().mergeTwoLists([0],[]))
