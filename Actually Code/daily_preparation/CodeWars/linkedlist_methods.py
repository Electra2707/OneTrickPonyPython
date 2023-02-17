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


def loop_size(node):
    tortoise = node.next
    hare = node.next.next
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next.next
    count = 1
    hare = hare.next
    while tortoise != hare:
        hare = hare.next
        count += 1
    return count


def stringify(node):
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    result.append("None")
    return " -> ".join(result)


def linked_list_from_string(string: str):
    if string == "None":
        return None
    elements = list(map(int, string.split(" -> ")[:-1]))
    head = None
    for i in reversed(range(len(elements))):
        head = Node(elements[i], head)
    return head


if __name__ == "__main__":
    print("Hello")
