#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = set()
        l = 0
        longest = 0
        for item in range(len(s)):
            while s[item] in table:
                table.remove(s[l])
                l+=1
            table.add(s[item])
            longest = max(len(table), longest)
        return longest 

# @lc code=end

