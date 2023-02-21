"""Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears
only once. Return the linked list sorted as well.
Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= ListNode.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        return Solution.list_to_node(sorted(list(Solution.node_to_set(head))))

    def node_to_set(head):
        if not head:
            return set()
        new_set = set()
        while head:
            new_set.add(head.val)
            head = head.next
        return new_set

    def list_to_node(lst: list):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for element in lst[1:]:
            current.next = ListNode(element)
            current = current.next
        return head
