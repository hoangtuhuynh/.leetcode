#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []
        stack = [(root, '')]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path + str(node.val))
            if node.right:
                stack.append((node.right, path + str(node.val) + '->'))
            if node.left:
                stack.append((node.left, path + str(node.val) + '->'))
           
        return res
# @lc code=end

