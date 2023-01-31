"""
Sum of Pairs
Given a list of integers and a single sum value, 
return the first two values (parse from the left please) 
in order of appearance that add up to form the sum.

If there are two or more pairs with the required sum, 
the pair whose second element has the smallest index 
is the solution.

Negative numbers and duplicate numbers can
and will appear.

NOTE: There will also be lists tested of 
lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.
"""
import numpy as np


def sum_pairs(ints: list[int], s: int):
    ints_np = np.array(ints)
    seen = set()
    for num in np.nditer(ints_np):
        target = s - num
        if target in seen:
            return [target, num.item()]
        seen.add(num.item())
    else:
        return None





# , [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
print(1, sum_pairs(l1, 8))
# , [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
print(2, sum_pairs(l2, -6))
# is None, "No Match: %s should return None for sum = -7" % l3)
print(3, sum_pairs(l3, -7))
# , [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
print(4, sum_pairs(l4, 2))
# , [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
print(5, sum_pairs(l5, 10))
# , [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
print(6, sum_pairs(l6, 8))
# , [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
print(7, sum_pairs(l7, 0))
# , [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)
print(8, sum_pairs(l8, 10))
# , [6, 7], "Ten Million Numbers With Middle Pair: Should terminate with a valid pair output")
print(9, sum_pairs(l9, 13))
# , [8, -3], "Ten Million Numbers With Pair At End: Should terminate with a valid pair output")
print(10, sum_pairs(l9, 5))
# , [13, 3], "Ten Million Numbers With Pair At Start: Should terminate with a valid pair output")
print(11, sum_pairs(l9, 16))
# is None, "Ten Million Numbers With No Match: Should return None in a decent time period")
print(12, sum_pairs(l9, 31))
