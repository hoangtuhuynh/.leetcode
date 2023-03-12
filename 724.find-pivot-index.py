#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            arr1 = nums[:i]
            arr2  = nums[i+1:]
            sum_1 = sum(arr1)
            sum_2 = sum(arr2)
            if sum_1 == sum_2:
                return i
                break
            else:
                pass
        return -1     
# @lc code=end

