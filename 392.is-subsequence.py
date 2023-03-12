#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)> len(t):
            return False
        if len(s) ==0:
            return True
        count = 0
        for i in range(len(t)):
            if count<= len(s)-1:
                if s[count] == t[i]:
                    count+=1
        if count == len(s):
            return True
        return False    
# @lc code=end

