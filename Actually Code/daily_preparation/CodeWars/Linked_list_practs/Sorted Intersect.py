"""Linked Lists All Methods
Write a SortedIntersect() function which creates and 
returns a list representing the intersection of two lists
that are sorted in increasing order. Ideally, each list should 
only be traversed once. The resulting list should not contain duplicates.

var first = 1 -> 2 -> 2 -> 3 -> 3 -> 6 -> null
var second = 1 -> 3 -> 4 -> 5 -> -> 6 -> null
sortedIntersect(first, second) === 1 -> 3 -> 6 -> null
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def sorted_intersect(first, second):
    first = node_to_set(first)
    second = node_to_set(second)
    third = first & second
    return list_to_node(sorted(list(third)))


def node_to_set(head):
    if not head:
        return set()
    new_set = set()
    while head:
        new_set.add(head.data)
        head = head.next
    return new_set


def list_to_node(lst: list):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for element in lst[1:]:
        current.next = Node(element)
        current = current.next
    return head


# def sorted_intersect(first, second):
#     intersection = []
#     current_first = first
#     current_second = second

#     while current_first is not None and current_second is not None:
#         if current_first.data == current_second.data:
#             if not intersection or current_first.data != intersection[-1]:
#                 intersection.append(current_first.data)
#             current_first = current_first.next
#             current_second = current_second.next
#         elif current_first.data < current_second.data:
#             current_first = current_first.next
#         else:
#             current_second = current_second.next

#     return create_linked_list(intersection)


# def create_linked_list(lst):
#     head = None
#     for value in reversed(lst):
#         head = Node(value, head)
#     return head
