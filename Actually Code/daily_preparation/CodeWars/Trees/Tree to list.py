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
