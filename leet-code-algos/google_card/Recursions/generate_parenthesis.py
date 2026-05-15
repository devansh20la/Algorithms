class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(A = [], left = 0, right = 0):
            if len(A) == 2*n:
                res.append("".join(A))
                return
            
            if left < n:
                A.append("(")
                backtrack(A, left + 1, right)
                A.pop()
            if right < left:
                A.append(")")
                backtrack(A, left, right + 1)
                A.pop()
        
        backtrack()
        return res