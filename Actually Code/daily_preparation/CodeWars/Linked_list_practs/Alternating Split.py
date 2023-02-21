"""Alternating Split
Write an AlternatingSplit() function that takes one list and divides
up its nodes to make two smaller lists. The sublists should be made
from alternating elements in the original list. So if the original 
list is a -> b -> a -> b -> a -> null then one sublist should be
a -> a -> a -> null and the other should be b -> b -> null.

list = 1 -> 2 -> 3 -> 4 -> 5 -> None
alternating_split(list).first == 1 -> 3 -> 5 -> None
alternating_split(list).second == 2 -> 4 -> None
For simplicity, we use a Context object to store and return 
the state of the two linked lists. A Context object containing
the two mutated lists should be returned by AlternatingSplit().
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if not head:
        raise Exception("Empty head")
    first_dummy = Node(0)
    second_dummy = Node(0)
    first_tail = first_dummy
    second_tail = second_dummy
    counter = 0
    while head:
        if counter % 2 == 0:
            first_tail.next = head
            first_tail = head
        else:
            second_tail.next = head
            second_tail = head
        counter += 1
        head = head.next
    if counter <= 1:
        raise Exception("Linked List too short")
    # Terminate each sublist with None
    first_tail.next = None
    second_tail.next = None
    return Context(first_dummy.next, second_dummy.next)


testing = alternating_split(
    Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))))


def node_to_string(node):
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    result.append("None")
    return " -> ".join(result)


print(node_to_string(testing.first))  # expected 1 -> 3 -> 5
print(node_to_string(testing.second))  # expected 2 -> 4 -> 6


# def alternating_split(head):
#     if not head:
#         raise Exception("Empty head")
#     first, second = Node(0), Node(0)
#     counter = 0
#     while head:
#         if counter % 2 == 0:
#             first.next = head
#             first = first.next

#         else:
#             second.next = head
#             second = second.next
#         counter += 1
#         head = head.next
#     if counter <= 1:
#         raise Exception("Linked List too short")
#     return Context(first.next, second.next)
