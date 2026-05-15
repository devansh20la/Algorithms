# number of islands
# https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs_search(i, j):
            grid[i][j] = "0"
            if 0<=i+1 < len(grid) and grid[i+1][j] == "1":
                dfs_search(i+1, j)
            if 0<=j+1 < len(grid[0]) and grid[i][j+1] == "1":
                dfs_search(i, j+1)
            if 0<=j-1 < len(grid[0]) and grid[i][j-1] == "1":
                dfs_search(i, j-1)
            if 0<=i-1 < len(grid) and grid[i-1][j] == "1":
                dfs_search(i-1, j)
    
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs_search(i, j)
                    res += 1
        
        return res