#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        for i in range(len(s)):

            #odd length
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)>length:
                    choose = s[l:r+1]
                l-=1
                r+=1
            
            #even length
            l, r = i, i+1
            while l>=0 and r< len(s) and s[l]==s[r]:
                if (r-l+1)>length:
                    choose = s[l:r+1]
                l-=1
                r+=1
        return choose
# @lc code=end

