"""Given an n x n grid containing only values 0 and 1,
where 0 represents water and 1 represents land, find 
a water cell such that its distance to the nearest land 
cell is maximized, and return the distance. If no land or
water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance:
the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""


class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        max_dist = -1
        # for dimension in grid:
        #     counter = -1
        #     if counter != -1:
        #         counter += 1
        #     while dimension:
        #         vertex = dimension.pop(0)
        #         if vertex == 1:
        #             counter = -1
        #         elif vertex == 0:
        #             counter += 1
        #             if counter > max_dist:
        #                 max_dist = counter
                        
        # visited = set()
        # for i, dimension in enumerate(grid):
        #     for j, element in enumerate(dimension):
        #         vertex = 

        return max_dist


print(Solution().maxDistance(
    [[1,0,0],[0,0,0],[0,0,0]]
))
