"""Linked Lists All Methods
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def build_one_two_three():
    linked_list = Node(1, Node(2, Node(3)))
    return linked_list


def push(head, data):
    new_node = Node(data, head)
    return new_node


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


def node_to_list(head):
    if head is None:
        return []
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result


def node_to_string(node):
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    result.append("None")
    return " -> ".join(result)


def stringInt_to_node(string: str):
    if string == "None":
        return None
    elements = list(map(int, string.split(" -> ")[:-1]))
    head = None
    for i in reversed(range(len(elements))):
        head = Node(elements[i], head)
    return head


def get_nth(node, index: int):
    counter = 0
    while node:
        if counter == index:
            return node
        node = node.next
        counter += 1
    raise Exception("index out of range")


def insert_nth(linked_list, index, data):
    if index == 0:
        return Node(data, linked_list)
    current = linked_list
    counter = 0
    while current:
        if counter == index-1:
            current.next = Node(data, current.next)
            return linked_list
        current = current.next
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


def sorted_insert(head, data):
    current = head
    if not current or data < current.data:
        return Node(data, head)
    while current.next and current.next.data < data:
        current = current.next
    current.next = Node(data, current.next)
    return head


def mergeTwoLists(l1, l2):
    head = current = Node(0)
    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return head.next


if __name__ == "__main__":
    print("Hello")
