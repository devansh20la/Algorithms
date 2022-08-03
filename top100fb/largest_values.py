# https://leetcode.com/problems/find-largest-value-in-each-tree-row
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        if root is None:
            return res

        while(len(stack) != 0):
            temp_max = float('-inf')
            for i in range(len(stack)):
                node = stack[i]
                if node.val > temp_max: temp_max = node.val
                if node.left: stack.append(node.left)    
                if node.right: stack.append(node.right)
            
            stack = stack[i+1:]
            res.append(temp_max)
        
        return res