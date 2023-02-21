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
    new_node = Node(0)
    while head:
        new_node = head
        new_node = new_node.next
        head = head.next
        return new_node