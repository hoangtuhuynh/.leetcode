#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for  i in nums1:
            nums2.append(i)
        nums2 = sorted(nums2)
        n = len(nums2) // 2
        if len(nums2) %2 != 0:
            return float(nums2[n])
        else:
            return float((nums2[n] + nums2[n-1])/2)
        
# @lc code=end

