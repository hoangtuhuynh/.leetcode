#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_value = 0
        while sell < len(prices):
            current_profit = prices[sell] - prices[buy]
            if current_profit>0:
                max_value = max(current_profit, max_value)
            else:
                buy = sell
            sell+=1
        return max_value    
# @lc code=end

