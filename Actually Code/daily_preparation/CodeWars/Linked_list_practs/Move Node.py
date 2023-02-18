"""Move Node
Write a MoveNode() function which takes the node from the
front of the source list and moves it to the front of the
destintation list. You should throw an error when the source
list is empty. For simplicity, we use a Context object to store 
and return the state of the two linked lists. A Context object
containing the two mutated lists should be returned by moveNode.

MoveNode() is a handy utility function to have for later problems.
source = 1 -> 2 -> 3 -> None
dest = 4 -> 5 -> 6 -> None
move_node(source, dest).source == 2 -> 3 -> None
move_node(source, dest).dest == 1 -> 4 -> 5 -> 6 -> None
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source, dest):
    if not source:
        raise Exception("Empty linked list")
    dest = Node(source.data, dest)
    source = source.next
    return Context(source, dest)


def list_to_node(lst: list):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for element in lst[1:]:
        current.next = Node(element)
        current = current.next
    return head


source1 = list_to_node([1, 2, 3])
dest1 = list_to_node([4, 5, 6])
testing = move_node(source1, dest1)
