#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        result = []
        while left!=right:
            sum = numbers[left] + numbers[right]
            if sum> target:
                right-=1
            elif sum<target:
                left+=1
            else:
                result.append(left+1)
                result.append(right+1)
                break
        return result
            
                
                
        


            
            
# @lc code=end

