#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        tem  = []
        def backtrack(open: int, close: int):
            if open == close == n:
                tem.append("".join(stack))
            if open<n:
                stack.append("(")
                backtrack(open+1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                backtrack(open, close+1)
                stack.pop()
        backtrack(0,0)
        return tem

# @lc code=end

