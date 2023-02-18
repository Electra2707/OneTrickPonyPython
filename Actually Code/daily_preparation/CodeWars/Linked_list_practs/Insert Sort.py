"""Insert Sort
Write an InsertSort() function which rearranges nodes
in a linked list so they are sorted in increasing order.
You can use the SortedInsert() function that you created 
in the "Linked Lists - Sorted Insert" kata below. The InsertSort()

var list = 4 -> 3 -> 1 -> 2 -> null
insertSort(list) === 1 -> 2 -> 3 -> 4 -> null
If the passed in head node is null or a single node,
return null or the single node, respectively. You can 
assume that the head node will always be either null, 
a single node, or a linked list consisting of multiple nodes.
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert_sort(head):
    sorted_list = sorted(node_to_list(head))
    return list_to_node(sorted_list)


def sorted_insert(head, data):
    current = head
    if not current or data < current.data:
        return Node(data, head)
    while current.next and current.next.data < data:
        current = current.next
    current.next = Node(data, current.next)
    return head


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


testing = insert_sort(list_to_node([7, 6, 5, 4, 3, 2, 1]))
print(node_to_list(testing))
