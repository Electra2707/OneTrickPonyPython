"""Iterative Reverse
Write an iterative Reverse() function that reverses a linked list. 
Ideally, Reverse() should only need to make one pass of the list.

var list = 2 -> 1 -> 3 -> 6 -> 5 -> null
reverse(list)
list === 5 -> 6 -> 3 -> 1 -> 2 -> null
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def reverse(head):
    if head is None: return None
    curr = head
    prev = None
    while curr:
        new_node = Node(curr.data)
        new_node.next = prev
        prev = new_node
        curr = curr.next
    
    head.data, head.next = prev.data, prev.next
    return head


# def reverse(head):
#     head = node_to_list(head)
#     return list_to_node(list(reversed(head)))


# def node_to_list(head):
#     if head is None:
#         return []
#     result = []
#     while head:
#         result.append(head.data)
#         head = head.next
#     return result


# def list_to_node(lst: list):
#     if not lst:
#         return None
#     head = Node(lst[0])
#     current = head
#     for element in lst[1:]:
#         current.next = Node(element)
#         current = current.next
#     return head


# # def reverse(head):
# #     previous = None
# #     current = head
# #     while current:
# #         next = current.next  # save next node
# #         current.next = previous  # reverse link
# #         previous = current  # update previous node
# #         current = next  # update current node
# #     head = previous  # update head pointer
# #     return head
# def string_to_node(string: str):
#     if string == "None":
#         return None
#     elements = list(map(int, string.split(" -> ")[:-1]))
#     head = None
#     for i in reversed(range(len(elements))):
#         head = Node(elements[i], head)
#     return head


# def node_to_string(node):
#     result = []
#     while node:
#         result.append(str(node.data))
#         node = node.next
#     result.append("None")
#     return " -> ".join(result)


# testing = string_to_node("3 -> 1 -> None")
# print(node_to_string(reverse(testing)))

#  2 -> 1 -> 3 -> 6 -> 5 -> null
#  curr = 2 -> 1 -> 3 -> 6 -> 5 -> null 
#  prev = None 
#  new_node = None

#  First iteration: 
#      new_node = Node(2) 
#      new_node.next = None
#      prev = 2 -> null 
#      curr = 1 -> 3 -> 6 -> 5 -> null

# Second iteration: 
#     new_node = Node(1) 
#     new_node.next = 2 -> null 
#     prev = 1 -> 2 -> null 
#     curr = 3 -> 6 -> 5 -> null

# Third iteration: 
#     new_node = Node(3) 
#     new_node.next = 1 -> 2-> null 
#     prev = 3->1->2->null 
#     curr=6->5->null

# Fourth iteration: 
#     new_node=Node(6) 
#     new_node.next=3->1->2->null 
#     prev=6->3->1->2->null 
#     curr=5->null

# Fifth iteration: 
#     new_node=Node(5) 
#     new_node.next=6->3->1->2-null 
#     prev=5-6-3-1-2-null 
#     curr=null

# After exiting loop: 
#     head.data=head.next=prev.data=prev.next (swap operation) head=5-6-3-1-2-null (result)