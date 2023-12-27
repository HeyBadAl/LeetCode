# Given an m*n 2D bindry grid `grid` which represents a map of '1's (land) and '0's (watter), return the number of islands
# An island is sorrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all our edges of the grid are all sorrounded by water.

"""
Clarifying questions:
    - input always a valid grid (rectangular)?
    - any contraints on the size of the grid?
    - modifying the grid is possible, or it's read only?

Approach:
    - create a recursive function, `dfs` which perform DFS starting from a given position `(i, j)`
    - iterate the entire grid, whenever we encouter a land (`1`), increment the island count and explore it using dfs.
    - return the number of islands

Time: 
    - O(m * n), m is the number of rows, n is the number of columns in the grid.
    - we visit each cell once.

Space:
    - O(1), we only modifying the input grid in-place.
    - dfs function is recursive and its depth is at most the maximum number of rows or columns,
    - so, spcae complexity due to the call stack os O(max(m, n))

"""


from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        def dfs(i, j):
            if (
                i < 0
                or i >= len(grid)
                or j < 0
                or j >= len(grid[0])
                or grid[i][j] == "0"
            ):
                return
            grid[i][j] = "0"  # Marking the current land as visited

            # Explore all four directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        island_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island_count += 1
                    dfs(i, j)

        return island_count


sol = Solution()

example_grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

result = sol.numIslands(example_grid)
print("Number of islands:", result)
