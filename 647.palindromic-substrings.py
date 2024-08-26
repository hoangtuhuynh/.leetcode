#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        length = 0
        count = 0

        for i in range(len(s)):
            
            # odd numbers
            l, r = i, i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)> length:
                    count+=1
                    
                l-=1
                r+=1
            
            # even number
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1)> length:
                    count+=1
                    
                l-=1
                r+=1
        return count


# @lc code=end

