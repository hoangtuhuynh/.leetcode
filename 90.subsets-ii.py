#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curSet = [], []
        self.helper(0, nums, subsets, curSet)
        return subsets

    def helper(self, i, nums, subsets, curSet):
        if i >= len(nums):
            subsets.append(curSet.copy())
            return 
        curSet.append(nums[i])
        self.helper(i+1, nums, subsets, curSet)
        curSet.pop()

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i+=1
        self.helper(i+1, nums, subsets, curSet)
        
# @lc code=end

