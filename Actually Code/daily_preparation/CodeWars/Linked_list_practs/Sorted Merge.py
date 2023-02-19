"""Sorted Merge
Write a SortedMerge() function that takes two lists, 
each of which is sorted in increasing order, and merges
the two together into one list which is in increasing order. 
SortedMerge() should return the new list. The new list should
be made by splicing together the nodes of the first two lists. 
Ideally, SortedMerge() should only make one pass through each list.
SortedMerge() is tricky to get right and it may be solved iteratively 
or recursively.

var first = 2 -> 4 -> 6 -> 7 -> null
var second = 1 -> 3 -> 5 -> 6 -> 8 -> null
sortedMerge(first, second) === 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 6 -> 7 -> 8 -> null

There are many cases to deal with: either 'first' or 'second'
may be null/None/nil, during processing either 'first' or 'second'
may run out first, and finally there's the problem of starting t
he result list empty, and building it up while going through 'first' and 'second'.

If one of the argument lists is null, the returned list should
be the other linked list (even if it is also null). No errors need 
to be thrown in SortedMerge().
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


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
