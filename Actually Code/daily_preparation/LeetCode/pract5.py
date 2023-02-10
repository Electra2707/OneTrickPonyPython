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


from collections import deque

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        max_dist = -1
        queue = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        if not queue or len(queue) == len(grid) * len(grid[0]):
            return max_dist
        while queue:
            i, j, dist = queue.popleft()
            max_dist = max(max_dist, dist)
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited:
                    queue.append((x, y, dist + 1))
                    visited.add((x, y))
        return max_dist
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

        return max_dist


print(Solution().maxDistance(
    [[1, 0, 1],
     [0, 0, 0],
     [1, 0, 1]]
))
