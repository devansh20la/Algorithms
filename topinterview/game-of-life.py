class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        
        def count_live_neighbors(board, i, j):
            res = 0
            for p,q in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                if -1 < i+p < m and -1 < j+q < n and abs(board[i+p][j+q]) == 1:
                    res+=1    
            return res
        
        for i in range(m):
            for j in range(n):
                
                current_cell = board[i][j]
                live_neighbors = count_live_neighbors(board, i, j)
                
                if current_cell == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1

                if current_cell == 0 and live_neighbors == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0