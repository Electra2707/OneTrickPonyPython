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
    # Your code goes here.
    # Remember to return the head of the list.
    pass


def sorted_insert(head, data):
    current = head
    if not current or data < current.data:
        return Node(data, head)
    while current.next and current.next.data < data:
        current = current.next
    current.next = Node(data, current.next)
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


def string_to_node(string: str):
    if string == "None":
        return None
    try:
        elements = list(map(int, string.split(" -> ")[:-1]))
    except ValueError:
        elements = list(string.split(" -> ")[:-1])
    head = None
    for i in reversed(range(len(elements))):
        head = Node(elements[i], head)
    return head


testing = sorted_insert(build_one_two_three(), 0)
print(node_to_list(testing))
testing = sorted_insert(build_one_two_three(), 4)
print(node_to_list(testing))
