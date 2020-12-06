# https://leetcode.com/problems/binary-tree-right-side-view
# binary-tree-right-side-view
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        stack, res = [root], []

        while(len(stack) !=0):
            s = len(stack)
            level = []
            for i in range(s):
                node = stack[i]
                level.append(node.val)

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(level[-1])
            if i != len(stack):
                stack = stack[i+1:]
            else:
                stack = []
        return res