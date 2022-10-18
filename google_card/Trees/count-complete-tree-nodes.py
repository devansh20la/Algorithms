# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def computeleftdepth(self, node):
        d = 1
        while node.left:
            node = node.left
            d+=1        
        return d

    def computerightdepth(self, node):
        d = 1
        while node.right:
            node = node.right
            d+=1
        return d
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        leftdepth = self.computeleftdepth(root)
        rightdepth = self.computerightdepth(root)
        
        if leftdepth == rightdepth:
            return 2**leftdepth - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1