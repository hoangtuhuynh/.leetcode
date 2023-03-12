#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        new_set = set(nums)
        length = 0 
        for num in nums:
            if (num-1) not in new_set:
                length = 1
                while (num+1) in new_set:
                    length+=1
                    num+=1
            count = max(count, length)
        return count    
# @lc code=end

