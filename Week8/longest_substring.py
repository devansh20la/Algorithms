# Longest substring
# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        j = 1
        max_len = 0
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0

        while(j < len(s)):
            if s[j] not in s[i:j]:
                j+=1
                if (j - i) > max_len:
                    max_len = (j-i)
            else:
                i+=1
        
        return max_len