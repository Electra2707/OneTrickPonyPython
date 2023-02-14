"""
Can you get the loop ?
You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop. Your objective is to determine the length of the loop.

For example in the following picture the size of the dangling piece is 3 and the loop size is 12:

Notes:

do NOT mutate the nodes!
in some cases there may be only a loop, with no dangling piece
Thanks to shadchnev, I broke all of the methods from the Hash class.

Don't miss dmitry's article in the discussion after you pass the Kata !! 
"""

# class Node(object):
#     def __init__(self, next=None):
#         self.next = next
# def loop_size(node):
#     pointer_1 = node.next
#     condition = 1
#     while True:
#         pointer_2 = pointer_1.next
#         if pointer_1 is pointer_2:
#             return condition
#         pointer_1 = pointer_1.next
#         condition += 1

# Make a short chain with a loop of 3
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
print(loop_size(node1))#, 3, 'Loop size of 3 expected')

# Make a longer chain with a loop of 29
nodes = [Node() for _ in range(50)]
for node, next_node in zip(nodes, nodes[1:]):
    node.next = next_node
nodes[49].next = nodes[21]
print(loop_size(nodes[0]))#, 29, 'Loop size of 29 expected')

# Make a very long chain with a loop of 1087
# chain = create_chain(3904, 1087)
# print(loop_size(chain)#), 1087, 'Loop size of 1087 expected')