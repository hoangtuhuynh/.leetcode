#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        dp = [0,0]
        for n in nums:
            tmp = max(dp[0]+n, dp[1])
            dp[0] = dp[1]
            dp[1] = tmp
        return dp[1] 
# @lc code=end

