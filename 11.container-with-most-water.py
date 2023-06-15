#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_result = 0
        left = 0
        right = len(height)-1
        while left!=right:
            width = right - left 
            if height[left]< height[right]:
                area = height[left] * width
                left+=1
            else:
                area = height[right] * width
                right-=1
            max_result = max(max_result, area)
        return max_result
        
# @lc code=end

