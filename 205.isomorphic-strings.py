#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict and t[i] not in t_dict:
                s_dict[s[i]] = t[i]
                t_dict[t[i]] = s[i]
            elif s[i] in s_dict and s_dict[s[i]] == t[i]:
                continue
            else:
                return False
            
        return True     
# @lc code=end

