#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tobeReplace = '`,.:;?!@#$%^&*()[]}\/{_-" '
        for i in tobeReplace:
            s = s.replace(i, '')
        s = s.replace('\'','')
        s = s.lower()

        if len(s) <= 1:
            return True
        left = 0
        right = len(s) - 1
        while left< right:
            if s[left]!= s[right]:
                return False
            left += 1
            right -= 1
        return True

        
# @lc code=end

