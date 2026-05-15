class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j, cache):
            if cache[i][j] != 0:
                return cache[i][j]
            path_len = 0            
            for p,q in [(-1,0), (0,-1), (1,0), (0,1)]:
                if -1< i+p < m and -1 < j+q < n and matrix[i][j] < matrix[i+p][j+q]:
                    path_len = max(path_len, dfs(i+p, j+q, cache))
            
            cache[i][j] = path_len+1
            return cache[i][j]
        
        m, n = len(matrix), len(matrix[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]
        max_path = 0
        for i in range(m):
            for j in range(n):
                 max_path = max(max_path, dfs(i, j, cache))       
        return max_path