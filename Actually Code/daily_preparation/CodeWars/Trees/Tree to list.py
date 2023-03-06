"""Tree to list
Given the root of a tree with an arbitrary number of child
nodes, return a list containing the nodes' data in
breadth-first order (left to right, top to bottom).

Child nodes are stored in a list. An empty tree is represented by an empty list.

Example:

           1
          / \
         2   3  -> [1,2,3,4,5,6,7]
        /|\   \
       4 5 6   7

"""


class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = [] if child_nodes is None else child_nodes


def tree_to_list(tree_root):
    if not tree_root:
        return []
    l1 = [tree_root.data]
    nodes = tree_root.child_nodes
    l2 = []
    while nodes:
        node = nodes.pop(0)
        l1.append(node.data)
        for element in node.child_nodes:
            l2.append(element)
        if not nodes:
            nodes = l2.copy()
            l2.clear()
    return l1


hello = Node(
    'H', [Node('e', [Node('l'), Node('o', [Node('w'), Node('!')])]), Node('l')])
# testing = Node(1, [Node(2, [Node(3), Node(4), Node(5)]), Node(3, [Node(7)])])
# print(tree_to_list(testing), "result \n[1, 2, 3, 3, 4, 5, 7] expected")
print(tree_to_list(hello),
      "result \n['H', 'e', 'l', 'l', 'o', 'w', '!'] expected")
