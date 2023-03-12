#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = {}
        count = [[] for num in range(len(nums)+1)]
        for num in nums:
            if num not in new_dict:
                new_dict[num] = 1
            else:
                new_dict[num]+=1
        for key,value in new_dict.items():
            count[value].append(key)
        new_list = []
        for j in range(len(nums), 0, -1):
            for n in count[j]:
                new_list.append(n)
        return new_list[:k]    
# @lc code=end

