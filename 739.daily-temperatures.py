#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result  = [0] * len(temperatures)
        stack = [] # pair of [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                result[stackIndex]  =(i - stackIndex)
            stack.append([t, i])
        return result
        
# @lc code=end

