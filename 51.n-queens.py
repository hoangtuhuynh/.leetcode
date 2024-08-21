#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        postDiag = set() # r+c
        preDiag = set() # r-c

        res = []
        board = [['.'] * n for i in range(n)]

        self.backtracking(0,n,board, res, cols, postDiag=postDiag, preDiag=preDiag)
        return res

    def backtracking(self, r, n, board, res, cols, postDiag, preDiag):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in cols or (r+c) in postDiag or (r-c) in preDiag:
                continue
            cols.add(c)
            postDiag.add(r+c)
            preDiag.add(r-c)
            board[r][c] = "Q"

            self.backtracking(r+1,n,board,res,cols, postDiag, preDiag)

            cols.remove(c)
            postDiag.remove(r+c)
            preDiag.remove(r-c)
            board[r][c] = "."

# @lc code=end

