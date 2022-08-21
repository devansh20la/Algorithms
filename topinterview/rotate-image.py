class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # reflect on horizontal axis:
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j] , matrix[i][j]
        
        # transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
