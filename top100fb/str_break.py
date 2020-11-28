from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def t_wordBreak(start):
            if start == len(s):
                return True

            for i in range(start + 1, len(s)+1):
                if i in memo:
                    return True
                else:
                    if s[start:i] in wordDict and t_wordBreak(i):
                            memo[start] = True
                            return True
            return False
        
        return t_wordBreak(0)

s = Solution()
print(s.wordBreak("leetcode", ["leet","code"]))