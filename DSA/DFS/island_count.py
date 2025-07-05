# https://leetcode.com/problems/number-of-islands/description/
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from typing import List

class Solution:
    def __init__(self):
        self.visited = set()

    def get_neighbours(self, grid: List[List[str]], i, j) -> list:
        adj = [(0,1), (0,-1), (1,0), (-1,0)]
        neighbors = []
        for n in adj:
            new_row = i + n[0]
            new_col = j + n[1]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == "1":
                neighbors.append((new_row, new_col))

        return neighbors

    def dfs(self, grid: List[List[str]], i, j):
        self.visited.add((i,j))
        for n in self.get_neighbours(grid, i, j):
            if n in self.visited:
                continue
            self.dfs(grid, n[0], n[1])

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        island_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in self.visited:
                    self.dfs(grid, i, j)
                    island_count += 1

        print(self.visited)
        return island_count
