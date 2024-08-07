import collections
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
   
        q = collections.deque()
        for i in range(rows):
            for j in range (cols):
                if grid[i][j] == 0:
                    q.append((i,j))
        self.dfs(grid, rows, cols, q)    
               

    def dfs(self, grid, rows, cols, q):


        
        while q:
            
            current_r, current_c = q.popleft()
            direction = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in direction:
                row, col  =current_r +dr, current_c+dc
                if (row in range(rows) and
                    col in range(cols) and
                    grid[row][col] == 2147483647 ):
                    
                    grid[row][col] = grid[current_r][current_c]+1
                    q.append((row,col))
