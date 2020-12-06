# BT pre order traversal

# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# this is faster
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        
        if root.val is not None:
            res += [root.val]

            if root.left is not None:
                res += self.preorderTraversal(root.left)

            if root.right is not None:
                res += self.preorderTraversal(root.right)
        
        return res


class Solution:
       
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if root is None:
            return []

        stack, res = [root], []

        while (len(stack) ! = 0):
            root = stack.pop()
            res.append(root)

            if root.right is not None:
                stack.append(root.right)

            if root.left is not None:
                stack.append(root.left)
        
        return res