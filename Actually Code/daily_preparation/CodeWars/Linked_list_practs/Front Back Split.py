"""Remove Front Back Split
Write a FrontBackSplit() function that takes one list and
splits it into two sublists — one for the front half, and 
one for the back half. If the number of elements is odd, the
extra element should go in the front list. For example, 
FrontBackSplit() on the list 2 -> 3 -> 5 -> 7 -> 11 -> null 
should yield the two lists 2 -> 3 -> 5 -> null and 7 -> 11 -> 
null. Getting this right for all the cases is harder than it
looks. You will probably need special case code to deal with 
lists of length < 2 cases.

var source = 1 -> 3 -> 7 -> 8 -> 11 -> 12 -> 14 -> null
var front = new Node()
var back = new Node()
frontBackSplit(source, front, back)
front === 1 -> 3 -> 7 -> 8 -> null
back === 11 -> 12 -> 14 -> null

You should throw an error if any of the arguments to 
FrontBackSplit are null or if the source list has < 2 nodes.

"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def front_back_split(source, front, back):
    source_length = length(source)
    if source_length == 2:
        front = source
        front.next = None
        back = source.next
        return front,back
    elif source_length <=1:
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


def length(node):
    length_counter = 0
    while node:
        length_counter += 1
        node = node.next
    return length_counter


def slicer(node, data):
    head = new_node = Node(0)
    while node:
        if node.data == data:
            new_node.next = node
            return head.next
        new_node.next = node
        node = node.next
        new_node = new_node.next
