#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            str1 = sorted(s)
            str2 = sorted(t)
            if str1 == str2:
                return True
        return False    
# @lc code=end

