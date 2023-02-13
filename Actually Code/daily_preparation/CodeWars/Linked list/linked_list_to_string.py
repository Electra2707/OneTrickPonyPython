"""Convert a linked list to a string
LINKED LISTS
RECURSION
ALGORITHMS


"""


class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(node):
    pass


stringify(Node(0, Node(1, Node(2, Node(3)))))#, '0 -> 1 -> 2 -> 3 -> None')#
stringify(None)#, 'None'
stringify(Node(0, Node(1, Node(4, Node(9, Node(16))))))#, '0 -> 1 -> 4 -> 9 -> 16 -> None')