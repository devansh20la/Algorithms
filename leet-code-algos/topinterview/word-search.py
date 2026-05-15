class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        k = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[k]:
                    k+=1
                    def dfs(i,j):
                        if k == len(word):
                            return True

                        if i<0 or j<0 or i>len(board) or j>len(board[0]):
                            return False

                        for interval in [(-1,0), (0,-1), (1,0), (0,1)]:
                            if board[i+interval[0]][j+interval[1]] == word[k]:
                                k+=1
                                return dfs(i+interval[0], j+interval[1])
                            else:
                                return False  
                
                    return dfs(i,j)