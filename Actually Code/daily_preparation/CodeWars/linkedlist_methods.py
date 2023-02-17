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


def length(node):
    length_counter = 0
    while node:
        length_counter += 1
        node = node.next
    return length_counter


def count(node, data):
    counter = 0
    while node:
        if node.data == data:
            counter += 1
        node = node.next
    return counter


def get_nth(node, index: int):
    counter = 0
    while node:
        if counter == index:
            return node
        node = node.next
        counter += 1
    raise Exception("index out of range")


if __name__ == "__main__":
    print("Hello")
