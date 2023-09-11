#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        temp = []
        holder = [i for i in s1 ]
        pointer = []

        dict = {}
        for i in s1:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] +=1


        for item in range(len(s2)):
            if s2[item] in dict.keys() and dict[s2[item]] >0:
                temp.append(s2[item])
                pointer.append(item)
                dict[s2[item]] -=1
        if len(holder) == len(temp):
            for i in range(len(pointer)-1):
                if pointer[i] +1 != pointer[i+1]:
                    return False
            return True
       
        
        # else:
        #     return False
# @lc code=end

