"""Your goal in this kata is to implement a difference function,
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list 
b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]"""


def array_diff(a: list, b: list):
    normal_procediment=True
    for numbers in a:
        sum_list = a.count(numbers)
        if sum_list >= 3:
            normal_procediment=False
    if normal_procediment:
        return list(set(a)-set(b)) # work 6,5,3,1
    # return list(set(a) ^ set(b)) # the test 1 and 3 works
    # return list(set(a) & set(b)) # the test 5 works


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
