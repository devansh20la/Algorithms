class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
                
                
        if len(stack) != 0:
            return False
        
        return True
                    