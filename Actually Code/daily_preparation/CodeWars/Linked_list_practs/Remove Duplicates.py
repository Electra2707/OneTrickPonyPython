"""Remove Duplicates
Write a RemoveDuplicates() function which takes a 
sorted in increasing order and deletes any duplicate
nodes from the list. Ideally, the list should only be 
traversed once. The head of the resulting list should be returned.

var list = 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> null
removeDuplicates(list) === 1 -> 2 -> 3 -> 4 -> 5 -> null
If the passed in list is null/None/nil, simply return null.

Note: Your solution is expected to work on long lists.
Recursive solutions may fail due to stack size limitations."""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def remove_duplicates(head):
    current = set(node_to_list(head))
    return list_to_node(sorted(list(current)))
    # # efficient version
    # if head is None:
    #     return None

    # current = head
    # while current.next is not None:
    #     if current.data == current.next.data:
    #         current.next = current.next.next
    #     else:
    #         current = current.next

    # return head



def node_to_list(head):
    if head is None:
        return []
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result


def list_to_node(lst: list):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for element in lst[1:]:
        current.next = Node(element)
        current = current.next
    return head
