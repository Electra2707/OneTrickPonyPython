"""Your goal in this kata is to implement a difference function,
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list 
b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]"""


def array_diff(a: list, b: list):
    # if not b: return a
    # if not a: return a
    return [x for x in a if x not in b]

test1 = array_diff([1, 2], [1])
# expected [2]") normal
test2 = array_diff([1, 2, 2], [1])
# expected [2,2]")
test3 = array_diff([1, 2, 2], [2])
# expected [1]") normal""
test4 = array_diff([1, 2, 2], [])
# expected [1,2,2]")
test5 = array_diff([], [1, 2])
#  expected []") normal
test6 = array_diff([1, 2, 3], [1, 2])
#  expected [3]") normal

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
print(test6)
