#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_list = []
        post_list = []
        product = []
        product1 = 1
        product2 = 1
        for i in range(len(nums)):
            
            product1= product1 * nums[i]
            pre_list.append(product1)
        for j in range(len(nums)-1,-1,-1):
            
            product2= product2 * nums[j]
            post_list.append(product2)
        post_list = post_list[::-1]
        for k in range(len(nums)):
            if k == 0:
                k+=1
                product.append(post_list[k])
            elif k == len(nums)-1:
                k-=1
                product.append(pre_list[k])
            else:
                pre = k-1
                post = k+1
                temp = pre_list[pre] * post_list[post]
                product.append(temp)
        return product    
# @lc code=end

