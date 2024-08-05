class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, 0, i, j, ROWS, COLS,path):
                        return True
                    
        return False
                    

    def dfs(self, board, word,index, i, j, r, c, path):
        if (i<0 or i>= r or j<0 or j>=c or board[i][j] != word[index] or (i,j) in path ):
            return False
        if index == len(word)-1:
            return True
        path.add((i,j))
        res =  (self.dfs(board, word, index + 1, i - 1, j, r, c, path)
            or self.dfs(board, word, index + 1, i + 1, j, r, c, path)
            or self.dfs(board, word, index + 1, i, j - 1, r, c, path)
            or self.dfs(board, word, index + 1, i, j + 1, r, c, path))
        path.remove((i, j))
        return res
        