"""Append
Write an Append() function which appends one linked 
list to another. The head of the resulting list should be returned.

var listA = 1 -> 2 -> 3 -> null
var listB = 4 -> 5 -> 6 -> null
append(listA, listB) === 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
If both listA and listB are null/NULL/None/nil, 
return null/NULL/None/nil. I
f one list is null/NULL/None/nil and the other is not,
simply return the non-null/NULL/None/nil list."""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


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
