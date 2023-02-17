"""Linked Lists All Methods
"""

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def push(head, data):
    new_node = Node(data, head)
    return new_node


def build_one_two_three():
    linked_list = Node(1, Node(2, Node(3)))
    return linked_list

if __name__=="__main__":
    print("Hello")