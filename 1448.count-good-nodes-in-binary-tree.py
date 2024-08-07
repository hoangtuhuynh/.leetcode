#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxval):
            if not node:
                return 0
            res = 1 if node.val >= maxval else 0
            maxval = max(node.val, maxval)

            res += dfs(node.left, maxval)
            res += dfs(node.right, maxval)
            return res
        return dfs(root, root.val)
        
       # @lc code=end

