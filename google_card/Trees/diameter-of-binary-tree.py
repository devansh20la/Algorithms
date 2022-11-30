# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def longestpath(node):
            if not node:
                return 0
            nonlocal diameter

            _leftpath = longestpath(node.left)
            _rightpath = longestpath(node.right)
                        
            diameter = max(diameter, _leftpath + _rightpath)
            
            return max(_leftpath, _rightpath) + 1
        
        longestpath(root)
        return diameter