"""Linked List Random Node
Given a singly linked list, return a random node's value 
from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head 
of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns
its value. All the nodes of the list should be equally likely to be chosen.

Constraints:

The number of nodes in the linked list will be in the range [1, 104].
-104 <= Node.val <= 104
At most 104 calls will be made to getRandom.
"""
from random import randint
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        while head:
            self.length += 1
            head = head.next

    def getRandom(self) -> int:
        if self.length == 0:
            return 0
        elif self.length == 1:
            return self.head.val
        random = randint(0, self.length)
        counter = 0
        head = self.head
        while head:
            counter += 1
            if counter == random:
                return head
            head = head.next
        # Your Solution object will be instantiated and called as such:
        # obj = Solution(head)
        # param_1 = obj.getRandom()
