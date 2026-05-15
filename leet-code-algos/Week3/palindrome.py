# palindrome
# https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        for i in s:
            if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
                new_s += i
        if len(new_s) == 1:
            return True
        for i in range(0, len(new_s)):
            if new_s[i] != new_s[-1-i]:
                return False
        return True