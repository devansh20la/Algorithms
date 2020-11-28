# most common word
# https://leetcode.com/problems/most-common-word

from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        has_map = {}
        banned = set(banned)
        paragraph = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        for w1 in paragraph.split():
            if w1 not in banned:
                if w1 in has_map:
                    has_map[w1] += 1
                else:
                    has_map[w1] = 1

        return max(has_map.items(), key = lambda x: x[1])[0]