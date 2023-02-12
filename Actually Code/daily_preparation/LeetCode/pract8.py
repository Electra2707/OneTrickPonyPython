"""Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


class Solution:
    def mergeTwoLists(self, list1: list[int], list2: list[int]) -> list:
        return list1.extend(list2)
        # if not list1 and not list2:
        #     return []
        # elif len(list1) <= 1 and len(list2)<= 1 :
        #     return list1 
        # result = []
        # for element in list([x1]+[x2] for x1, x2 in zip(list1,list2)):
        #     for integral in element:
        #         result.append(integral)
        # return result 
        

print(Solution().mergeTwoLists([1,2,4],[1,3,4]))
print(Solution().mergeTwoLists([],[]))
print(Solution().mergeTwoLists([],[0]))