#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'2': 'abc', '3': 'def', '4': 'ghi',
                '5': 'jkl', '6': 'mno', '7': 'pqrs',
                '8': 'tuv', '9': 'wxyz'}
        res = []
        if len(digits) == 0:
            return res
        self.helperCombinations(digits, res, dict, '', 0)
        return res
    
    def helperCombinations(self, digits, res, dict, path, index):
        if index>=len(digits):
            res.append(path)
            return  
        string = dict[digits[index]]
        for i in string:
            self.helperCombinations(digits, res, dict, path+i, index+1)
        
# @lc code=end
        
# @lc code=end

