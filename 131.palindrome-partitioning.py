#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current = []
        self.dfs(res, current, 0, s)
        return res
    
    def dfs(self, res, current, i, s):
        if i>= len(s):
            res.append(current.copy())
            return 
        for j in range(i, len(s)):
            if self.Palind(s, i, j):
                current.append(s[i:j+1])
                self.dfs(res, current, j+1, s)
                current.pop()
    def Palind(self,s, l, r):
        while l<r:
            if s[l]!= s[r]:
                return False
            l, r = l+1, r-1
        return True

# @lc code=end

