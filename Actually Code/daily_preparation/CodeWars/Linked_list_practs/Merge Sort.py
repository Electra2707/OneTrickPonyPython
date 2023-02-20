"""Remove Duplicates
Write a MergeSort() function which recursively sorts a 
list in ascending order. Note that this problem requires recursion.
Given FrontBackSplit() and SortedMerge(), you can write a classic 
recursive MergeSort(). Split the list into two smaller lists, 
recursively sort those lists, and finally merge the two sorted lists
together into a single sorted list. Return the list."""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def merge_sort(list):
    list = node_to_list(list)
    return list_to_node(sorted(list))


def node_to_list(head):
    if head is None:
        return []
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result


def list_to_node(lst: list):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for element in lst[1:]:
        current.next = Node(element)
        current = current.next
    return head
