#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = cols-1
        if len(matrix) ==1:
            choose = 0
        for i in range(1,rows):
            if matrix[i][cols-1] >= target and matrix[i-1][cols-1] < target:
                choose = i
                break
            else:
                choose = 0
        while left<=right :
            middle = (right+left)//2
            if matrix[choose][middle]< target:
                left = middle+1
            elif matrix[choose][middle]> target:
                right = middle-1
            else:
                return True
        return False

        
# @lc code=end

