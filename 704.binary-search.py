#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        limit= float('inf')
        while limit>1:
            limit = right - left
            mid = (left + right) //2
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return int(-1)
# @lc code=end

