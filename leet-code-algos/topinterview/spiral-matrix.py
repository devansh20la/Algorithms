class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m,n = len(matrix), len(matrix[0])
        top, down, left, right = 0, m - 1, 0, n - 1
        res = []
        while len(res) < m*n:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
                        
            for row in range(top + 1,down + 1):
                res.append(matrix[row][right])
            
            if top!=down:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[down][col])
            
            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, top, -1):
                    res.append(matrix[row][left])
        
            left += 1
            right -= 1
            top += 1
            down -= 1

        return res
            
        
          