class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.N = len(words[0])
        self.hash_map = defaultdict(list)
        for word in words:
            for i in range(self.N):
                self.hash_map[word[:i]].append(word)

        self.results = []
        
        for word in words:
            word_squares = [word]
            self.backtracking(1, words, word_squares)
        
        return self.results
    
    def backtracking(self, step, words, word_squares):

        if step == self.N:
            self.results.append(word_squares[:])
            return
        prefix = "".join([word[step] for word in word_squares])
        
        # find words that start with prefix
        for candidate in self.hash_map[prefix]:
            word_squares.append(candidate)
            self.backtracking(step + 1, words, word_squares)
            word_squares.pop()
        
        return