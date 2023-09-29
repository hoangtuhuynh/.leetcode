#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
import collections
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        for row in range(rows):
            for column in range(columns):
                if (grid[row][column] == 1 and 
                    (row, column) not in visited):
                    current_area = 1
                    current_area = self.dfs(grid, row, column, visited, rows, columns, current_area)
                    max_area = max(max_area, current_area)
        return max_area
                 
    
    def dfs(self, grid, row, column, visited, rows, columns, area):
        q = collections.deque()
        visited.add((row, column))
        q.append((row, column))

        while q:
            r, c = q.popleft()
            direction = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in direction:
                current_row, current_column = r+dr, c+dc
                if (current_row in range(rows) and
                    current_column in range(columns) and
                    grid[current_row][current_column] == 1 and
                    (current_row, current_column) not in visited):
                    area+=1
                    visited.add((current_row, current_column))
                    q.append((current_row, current_column))

        return area

# @lc code=end
