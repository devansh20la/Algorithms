class Solution:
    def compress(self, word: str):
        letters, counts = [], []
        for c in word:
            if not letters or c != letters[-1]:
                letters.append(c)
                counts.append(1)
            else:
                counts[-1] += 1
        
        return letters, counts
                
    def check_if_stretchy(self, s_letters: List[str], s_counts: List[int], w: str) -> int:   
        w_letters, w_counts = self.compress(w)
        
        if w_letters != s_letters:
            return 0
        else:
            for i in range(len(w_letters)):
                if s_counts[i] < 3 and s_counts[i] != w_counts[i]:
                    return 0
                if s_counts[i] >= 3 and s_counts[i] < w_counts[i]:
                    return 0
            return 1
        
    def expressiveWords(self, s: str, words: List[str]) -> int:
        s_letters, s_counts = self.compress(s)
                
        result = 0
        
        for w in words:
            result += self.check_if_stretchy(s_letters, s_counts, w)
            
        return result