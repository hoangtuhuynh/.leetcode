#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
import collections
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, columns = len(grid), len(grid[0])
        visit = set()
        island = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visit:
                    self.bfs(r,c, visit,rows,columns, grid)
                    island += 1
        return island
    
    def bfs(self, r, c, visit, rows, columns, grid):
        q = collections.deque()
        visit.add((r, c))
        q.append((r, c))

        while q:
            row, column = q.popleft()
            directions =  [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                r, c = dr+row, dc+column
                if (r in range(rows) and 
                    c in range(columns) and
                    grid[r][c] == "1" and
                    (r, c) not in visit):
                    visit.add((r, c))
                    q.append((r, c))



# @lc code=end

