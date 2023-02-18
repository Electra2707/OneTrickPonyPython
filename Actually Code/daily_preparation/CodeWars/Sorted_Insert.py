"""Linked Lists All Methods
Write a SortedInsert() function which inserts a node 
into the correct location of a pre-sorted linked list 
which is sorted in ascending order. SortedInsert takes 
the head of a linked list and data used to create a
node as arguments. SortedInsert() should also return
the head of the list.

sortedInsert(1 -> 2 -> 3 -> null, 4) === 1 -> 2 -> 3 -> 4 -> null)
sortedInsert(1 -> 7 -> 8 -> null, 5) === 1 -> 5 -> 7 -> 8 -> null)
sortedInsert(3 -> 5 -> 9 -> null, 7) === 3 -> 5 -> 7 -> 9 -> null)

"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def sorted_insert(head, data):
    current = head
    if not current or data < current.data:
        return Node(data,head)
    while current.next and current.next.data < data:
        current = current.next
    current.next = Node(data,current.next)
    return head


def build_one_two_three():
    linked_list = Node(1, Node(2, Node(3)))
    return linked_list


def node_to_list(head):
    if head is None:
        return []
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result


testing = sorted_insert(build_one_two_three(), 0)
print(node_to_list(testing))
testing = sorted_insert(build_one_two_three(), 4)
print(node_to_list(testing))

