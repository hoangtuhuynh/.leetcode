#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if j != i:
                    sum = nums[i]+nums[j]
                    if sum==target:
                        return [i,j]
# @lc code=end

