class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'

        trie = {}
        for w in words:
            node = trie
            for l in w:
                node = node.setdefault(l, {})
            node[WORD_KEY] = w
        
        matched_words = []
        def backtrack(i, j, parent):
            letter = board[i][j]
            node = parent[letter]
            
            if WORD_KEY in node:
                matched_words.append(node[WORD_KEY])
                node.pop(WORD_KEY)
            
            board[i][j] = '#'
            
            for p,q in [(0,1), (1,0), (0, -1), (-1, 0)]:            
                if -1 < i+p < len(board) and -1 < j + q < len(board[0]) and board[i+p][j+q] in node:
                    backtrack(i+p, j+q, node)
            
            board[i][j] = letter
            
            if not node:
                parent.pop(letter)
        
        for i in range(len(board)):
            for j in range(len(board[0])):                
                if board[i][j] in trie:
                    backtrack(i, j, trie)
        
        return matched_words