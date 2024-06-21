#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubTree(root.left, subRoot) or self.isSubTree(root.right, subRoot)
        
    def isSameTree(self, r, s)->bool:
        if not r and not s:
            return True
        if not r or not s:
            return False
        
        if r.val != s.val:
            return False
        return self.isSameTree(r.left, s.left) and self.isSameTree(r.right, s.right)
        
            

# @lc code=end

