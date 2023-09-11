#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, current, total):
            if total == target:
                res.append(current.copy())
                return 
            if total >target or i>= len(candidates):
                return
            
            # the first decision function
            current.append(candidates[i])
            dfs(i, current, total+ candidates[i])

            # the second decision function
            current.pop()
            dfs(i+1, current, total)

        dfs(0, [], 0)
        return res
        
# @lc code=end

