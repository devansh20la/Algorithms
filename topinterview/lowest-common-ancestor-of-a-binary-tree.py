# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.parent = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def search(current_node):
            
            if current_node is None:
                return False
            
            left = search(current_node.left)
            right = search(current_node.right)              
            
            mid = current_node == p or current_node == q
            
            if mid + left + right >= 2:
                self.parent = current_node
            
            return mid or left or right
        
        search(root)
        return self.parent