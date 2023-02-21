"""Iterative Reverse
Write an iterative Reverse() function that reverses a linked list. 
Ideally, Reverse() should only need to make one pass of the list.

var list = 2 -> 1 -> 3 -> 6 -> 5 -> null
reverse(list)
list === 5 -> 6 -> 3 -> 1 -> 2 -> null
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse(head):
    previous = None
    current = head
    while current:
        next = current.next  # save next node
        current.next = previous  # reverse link
        previous = current  # update previous node
        current = next  # update current node
    head = previous  # update head pointer
    return head
