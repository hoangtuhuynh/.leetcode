#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], nums[1:], nums[:-1])

    def helper(self,nums):
        dp = [0, 0]
        for num in nums:
            temp = max(dp[0]+num, dp[1])
            dp[0] = dp[1]
            dp[1] = temp

        return dp[1]
        
# @lc code=end

