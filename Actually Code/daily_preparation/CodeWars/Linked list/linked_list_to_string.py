"""Convert a linked list to a string
LINKED LISTS
RECURSION
ALGORITHMS
"""


class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# def stringify(node):
#     if node is None:
#         return "None"
#     else:
#         string = str(node.data) + "->"
#         return string + stringify(node.next)

def stringify(node):
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    result.append("None")
    return " -> ".join(result)


print(stringify(Node(0, Node(1, Node(2, Node(3))))))#, '0 -> 1 -> 2 -> 3 -> None')#
print("----------------------------")
print(stringify(None))#, 'None'
print("----------------------------")
print(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))))#, '0 -> 1 -> 4 -> 9 -> 16 -> None')