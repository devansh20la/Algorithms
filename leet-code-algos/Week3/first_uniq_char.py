# first unique character in a string
# https://leetcode.com/problems/first-unique-character-in-a-string
# O(2n)
# O(1) only 26 english characted
class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniq = {}
        prev_c = None
        for index,c in enumerate(s):
            if c not in uniq:
                uniq[c] = 1
            else:
                uniq[c] += 1
        for index,c in enumerate(s):
            if uniq[c] == 1:
                return index
        return -1