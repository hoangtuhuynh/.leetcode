#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxleft = height[left]
        maxright = height[right]
        sum = 0
        while left<right:
            if maxleft<maxright:
                left+=1
                maxleft = max(maxleft, height[left])
                sum += maxleft - height[left]
            else:
                right-=1
                maxright = max(maxright, height[right])
                sum += maxright - height[right]
            
        return sum
            


        
# @lc code=end

