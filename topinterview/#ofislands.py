class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        islands = 0
        
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != "1":
                return
            
            grid[i][j] = "#"
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands += 1
        
        return islands
        