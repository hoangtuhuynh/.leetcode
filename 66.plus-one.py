#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''.join(str(digit) for digit in digits)
        new_val = eval(string+'+1')
        new_list = [int(digit) for digit in str(new_val)]
        return new_list
# @lc code=end

