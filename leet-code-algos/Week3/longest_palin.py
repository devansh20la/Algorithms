# longest palin
# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extend_out(l,r):
            while(l>=0 and r<len(s) and s[l] == s[r]):
                l-=1
                r+=1
            return l+1, r
        if len(s) == 1:
            return s
        if len(s) == 0:
            return ""
        start = 0
        end = 0
        p_len = 0
        for i in range(len(s) - 1):
            l, r = extend_out(i,i)
            if (r - l) > p_len:
                p_len = r - l
                start = l
                end = r
            l, r = extend_out(i,i+1)
            if (r - l) > p_len:
                p_len = r - l
                start = l
                end = r
        return s[start:end]
            
        

                
        