#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        candidates.sort()
        self.helperSum2(0, [], comb, candidates, target)
        return comb
    
    def helperSum2(self, i, curComb, comb, candidates, target):
        if target == 0:
            comb.append(curComb.copy())
            return
        if target <=0:
            return 
        prev = -1
        for j in range(i, len(candidates)):
            if candidates[j]== prev:
                continue
            
            curComb.append(candidates[j])
            self.helperSum2(j+1, curComb, comb, candidates, target - candidates[j])
            curComb.pop()
            prev = candidates[j]
            

        
# @lc code=end

