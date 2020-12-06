# BT post order traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        if root.left is not None:
            res += self.postorderTraversal(root.left)

        if root.right is not None:
            res += self.postorderTraversal(root.right)
        res += [root.val]
        return res

class Solution(object):
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, output = [root, ], []
        while len(stack) != 0:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
                
        return output[::-1]