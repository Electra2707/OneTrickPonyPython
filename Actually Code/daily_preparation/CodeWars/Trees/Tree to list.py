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
    l1 = [tree_root.data]
    nodes = tree_root.child_nodes
    while nodes:
        curr = nodes.pop()
        l1.append(curr.data)
        if curr.child_nodes:
            for element in curr.child_nodes:
                nodes.append(element)
    return sorted(l1)


testing = Node(1, [Node(2, [Node(3), Node(4), Node(5)]), Node(3, [Node(7)])])
print(tree_to_list(testing), "result \n[1, 2, 3, 3, 4, 5, 7] expected")
