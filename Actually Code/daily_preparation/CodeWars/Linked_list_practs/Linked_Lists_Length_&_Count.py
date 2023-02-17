"""Linked Lists - Length & Count
Implement Length() to count the number of nodes in a linked list.

length(null) => 0
length(1 -> 2 -> 3 -> null) => 3
Implement Count() to count the occurrences of an integer in a linked list.

count(null, 1) => 0
count(1 -> 2 -> 3 -> null, 1) => 1
count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4
I've decided to bundle these two functions within the same Kata since they are both very similar.

The push()/Push() and buildOneTwoThree()/BuildOneTwoThree() functions do not need to be redefined.
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
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


node_list = None
for i in range(3, 0, -1):
    node = Node(i)
    node.next = node_list
    node_list = node

node_list_r = None
for i in [3, 2, 1]:
    if i == 3:
        for j in range(2):
            node = Node(i)
            node.next = node_list_r
            node_list_r = node
    else:
        for j in range(4):
            node = Node(i)
            node.next = node_list_r
            node_list_r = node

node = None

print(length(node))
print(count(node,2))
print(length(node_list))
print(count(node_list,1))
print(length(node_list_r))
print(count(node_list_r,3))
# node_list = Node(1)
# node_list.next = Node(2)
# node_list.next.next = Node(3)
# node_list.next.next.next = None
# node_list_r = Node(1)
# node_list_r.next = Node(1)
# node_list_r.next.next = Node(1)
# node_list_r.next.next.next = Node(1)
# node_list_r.next.next.next.next = Node(2)
# node_list_r.next.next.next.next.next = Node(2)
# node_list_r.next.next.next.next.next.next = Node(2)
# node_list_r.next.next.next.next.next.next.next = Node(2)
# node_list_r.next.next.next.next.next.next.next.next = Node(3)
# node_list_r.next.next.next.next.next.next.next.next.next = Node(3)


# while node_list:
#     print(node_list.data)
#     node_list = node_list.next
# print("------------------")
# while node_list_r:
#     print(node_list_r.data)
#     node_list_r = node_list_r.next