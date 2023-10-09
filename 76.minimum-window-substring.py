#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        countT , window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        res , lenRes = [-1, -1], float("infinity")
        have, need = 0, len(countT)

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have+=1
            while have == need:
                if (r-l+1) < lenRes:
                    res = [l, r]
                    lenRes = r-l+1
                window[s[l]] -=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        l, r = res
        return s[l: r+1] if lenRes != float("infinity") else ""

                



        
# @lc code=end

