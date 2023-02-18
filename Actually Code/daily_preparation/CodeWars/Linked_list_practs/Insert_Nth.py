""" Insert Nth Node
Implement an InsertNth() function (insert_nth() in PHP)
which can insert a new node at any index within a list.

InsertNth() is a more general version of the Push() 
function that we implemented in the first kata listed below. 
Given a list, an index 'n' in the range 0..length, and a data
element, add a new node to the list so that it has the given index. 
InsertNth() should return the head of the list.

insertNth(1 -> 2 -> 3 -> null, 0, 7) === 7 -> 1 -> 2 -> 3 -> null)
insertNth(1 -> 2 -> 3 -> null, 1, 7) === 1 -> 7 -> 2 -> 3 -> null)
insertNth(1 -> 2 -> 3 -> null, 3, 7) === 1 -> 2 -> 3 -> 7 -> null)

You must throw/raise an exception 
(ArgumentOutOfRangeException in C#, InvalidArgumentException in PHP)
if the index is too large.

The push() and buildOneTwoThree() (build_one_two_three() in PHP) 
functions do not need to be redefined.
The Node class is also preloaded for you in PHP.
"""

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def node_to_string(node):
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    result.append("None")
    return " -> ".join(result)


def insert_nth(linked_list, index, data):
    if index == 0:
        return Node(data,linked_list)
    current = linked_list
    counter = 0
    while current:
        if counter == index-1:
            current.next = Node(data,current.next)
            return linked_list
        current = current.next
        counter += 1
    raise Exception("index out of range")
    # Your code goes here.
    # Return the head of the list.

testing = insert_nth(Node(1,Node(2)),3,4)
print(node_to_string(testing))