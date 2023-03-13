"""Add Binary
You are given two non-empty linked lists representing two
non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers
and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         num1 = []
#         num2 = []
#         while l1:
#             num1.insert(0, l1.val)
#             l1 = l1.next
#         while l2:
#             num2.insert(0, l2.val)
#             l2 = l2.next
#         l3 = int("".join([str(x) for x in num1])) + \
#             int("".join([str(x) for x in num2]))
#         head, tail = None, None
#         for i in reversed(str(l3)):
#             newnode = ListNode(i)
#             if head is None:
#                 head = newnode
#             else:
#                 tail.next = newnode
#             tail = newnode
#         return head

class Solution:
    def addTwoNumbers(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize head and tail as None
        head = None
        tail = None
        # Initialize carry as 0
        carry = 0
        # Iterate over both linked lists until both are None
        while first or second:
            # Get the values of current nodes or 0 if None
            x = first.val if first else 0
            y = second.val if second else 0
            # Calculate the sum of current digits and carry
            sum = x + y + carry
            # Update carry as quotient of sum divided by 10
            carry = sum // 10
            # Create a new node with remainder of sum modulo 10
            node = ListNode(sum % 10)
            # If head is None, set it as the new node
            if head is None:
                head = node
            # Else, set the next pointer of tail as the new node
            else:
                tail.next = node
            # Update tail as the new node
            tail = node
            # Move to next nodes if not None
            if first:
                first = first.next
            if second:
                second = second.next
        # If carry is not zero, add one more node with carry value
        if carry > 0:
            tail.next = ListNode(carry)
        # Return head as the linked list
        return head


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(Solution().addTwoNumbers(l1, l2))
