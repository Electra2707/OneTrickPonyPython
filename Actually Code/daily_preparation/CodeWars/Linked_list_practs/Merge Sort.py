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
    # Your code goes here.