"""Linked Lists All Methods
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# def build_one_two_three():
#     linked_list = Node(1, Node(2, Node(3)))
#     return linked_list


# def push(head, data):
#     new_node = Node(data, head)
#     return new_node


# class Context(object):
#     def __init__(self, source, dest):
#         self.source = source
#         self.dest = dest


# def move_node(source, dest):
#     if not source:
#         raise Exception("Empty linked list")
#     dest = Node(source.data,dest)
#     source = source.next
#     return Context(source, dest)


def append(listA, listB):
    if not listA and not listB:
        return None
    elif not listB:
        return listA
    elif not listA:
        return listB
    head = listA
    while listA.next:
        listA = listA.next
    listA.next = listB
    return head


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


def slicer(node, data):
    head = new_node = Node(0)
    while node:
        if node.data == data:
            new_node.next = node
            return head.next
        new_node.next = node
        node = node.next
        new_node = new_node.next


def reverse(head):
    previous = None
    current = head
    while current:
        next = current.next  # save next node
        current.next = previous  # reverse link
        previous = current  # update previous node
        current = next  # update current node
    head = previous  # update head pointer
    return head


def list_to_node(lst: list):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for element in lst[1:]:
        current.next = Node(element)
        current = current.next
    return head


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


def string_to_node(string: str):
    if string == "None":
        return None
    elements = list(map(int, string.split(" -> ")[:-1]))
    head = None
    for i in reversed(range(len(elements))):
        head = Node(elements[i], head)
    return head


def node_to_set(head):
    if not head:
        return set()
    new_set = set()
    while head:
        new_set.add(head.data)
        head = head.next
    return new_set


def remove_duplicates(head):
    return list_to_node(sorted(list(node_to_set(head))))
    # # efficient version
    # if head is None:
    #     return None

    # current = head
    # while current.next is not None:
    #     if current.data == current.next.data:
    #         current.next = current.next.next
    #     else:
    #         current = current.next

    # return head


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


def merge_sort(list):
    list = node_to_list(list)
    return list_to_node(sorted(list))


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


def insert_sort(head):
    sorted_list = sorted(node_to_list(head))
    return list_to_node(sorted_list)
    # # efficient version
    # if not head or not head.next:
    #     return head
    # new_head = Node(0)
    # current = head
    # while current:
    #     new_head = sorted_insert(new_head, current.data)
    #     current = current.next
    # return new_head.next


def sorted_intersect(first, second):
    first = node_to_set(first)
    second = node_to_set(second)
    third = first & second
    return list_to_node(sorted(list(third)))


def shuffle_merge(first, second):
    if not first and not second:
        return None
    elif not first:
        return second
    elif not second:
        return first
    head = current = Node(0)
    counter = 0
    while first and second:
        if counter % 2 == 0:
            current.next = first
            first = first.next
        else:
            current.next = second
            second = second.next
        counter += 1
        current = current.next
    current.next = first or second
    return head.next


def sorted_merge(l1, l2):
    if not l1 and not l2:
        return None
    elif not l1:
        return l2
    elif not l2:
        return l1
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


def front_back_split(source, front, back):
    source_length = length(source)
    if source_length == 2:
        front = source
        front.next = None
        back = source.next
        return front, back
    elif source_length <= 1:
        raise Exception("source too short")
    source_length = source_length // 2
    counter = 0
    current = source
    while current:
        if counter == source_length:
            front = slicer(source, current.data)
            back = current.next
            return front, back
        current = current.next
        counter += 1


if __name__ == "__main__":
    print("Hello")
