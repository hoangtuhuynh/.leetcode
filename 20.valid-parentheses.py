#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {')': '(', ']': '[', '}': '{'}
        open = ['(', '[', '{']
        stack = []
        if len(s) == 1 or s[0] not in open:
            return False
        for i in s:   
            if i in open:
               stack.append(i)
            else:
                if len(stack) == 0:
                    stack.append(i)
                temp = stack.pop()
                if temp!= dict[i]:
                    return False
        return len(stack) == 0
        
# @lc code=end

