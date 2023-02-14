"""
Linked Lists - Get Nth Node
Implement a GetNth() function that takes a linked list and an integer index
and returns the node stored at the Nth index position.
GetNth() uses the C numbering convention that the first node is index 0,
the second is index 1, ... and so on.

So for the list 42 -> 13 -> 666, GetNth(1) should return Node(13);

getNth(1 -> 2 -> 3 -> null, 0).data === 1
getNth(1 -> 2 -> 3 -> null, 1).data === 2
The index should be in the range [0..length-1]. If it is not, or 
if the list is empty, GetNth() should throw/raise an exception
(ArgumentException in C#, InvalidArgumentException in PHP, Exception in Java).
"""


class Node(object):
    index = 0

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.index = Node.index
        Node.index += 1


def get_nth(node, index:int):
    while node:
        if node.index == index:
            return node.data
        node = node.next

print(get_nth(Node(42,Node(13,Node(666))), 1))#.data === 1)