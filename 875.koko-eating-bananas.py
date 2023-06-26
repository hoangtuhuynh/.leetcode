#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
import math
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            sum = 0
            mid = (left + right)//2
            for item in range(len(piles)):
                sum += math.ceil(piles[item]/mid)
            if sum<= h:
                result = min(result,mid)
                right = mid-1
            else:
                left = mid+1
        return result
            
                


# @lc code=end

