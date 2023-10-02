#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
import collections
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res = []
        rows, columns = len(heights), len(heights[0])
        
        for row in range(rows):
            for col in range(columns):
                if(self.dfs(row, col, heights, rows, columns)):
                    res.append([row, col])
        return res

    
    def dfs(self, row, col, heights, rows, columns):
        pacific = False
        atlantic = False
        visited = set()
        q = collections.deque()
        visited.add((row, col))
        q.append([row, col])

        while q:
            cur_row, cur_col = q.popleft()
            if cur_row == 0 or cur_col == 0:
                pacific = True
            if cur_row == rows - 1 or cur_col == columns - 1:
                atlantic = True
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                r, c = cur_row + dr, cur_col + dc
                if (r in range(rows) and c in range(columns)
                    and heights[r][c]<=heights[cur_row][cur_col]
                    and (r,c) not in visited):
                        q.append([r, c])
                        visited.add((r,c))
        return (pacific and atlantic)                    

# @lc code=end

