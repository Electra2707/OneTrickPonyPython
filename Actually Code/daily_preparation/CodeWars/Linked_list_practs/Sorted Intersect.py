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
#     new_node = Node(0)
#     pointer_1 = first
#     pointer_2 = second
#     seen = set()
#     check = []
#     counter = 1
#     while pointer_1 and pointer_2:
#         check.append(pointer_1.data)
#         check.append(pointer_2.data)
#         if check[0] == check[1] and check[0] not in seen:
#             new_node.next = Node(check[0])
#             new_node = new_node.next
#             seen.add(check[0])
#         check.clear()
#         if pointer_1.next is None:
#             pointer_1 = pointer_1.next
#             continue
#         elif pointer_2.next is None:
#             pointer_2 = pointer_2.next
#             continue
#         if pointer_1.data == pointer_1.next.data:
#             pointer_1 == pointer_1.next
#             continue
#         elif pointer_2.data == pointer_2.next.data:
#             pointer_2 == pointer_2.next
#             continue
#         if counter % 2 == 0:
#             pointer_1 = pointer_1.next
#         else:
#             pointer_2 = pointer_2.next
#         counter += 1
#     return new_node.next


# def sorted_intersect(first, second):
#     New_Node = Node(0)
#     while first and second:
#         if first.data == second.data:
#             New_Node.next = first
#             New_Node = New_Node.next
#             if not first.data == first.next.data:
#                 first = first.next
#         if not second.data == second.next.data:
#             second = second.next
#     return New_Node.next
