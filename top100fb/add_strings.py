# Add strings
# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        while(i>=0 or j>=0):
            k1 = ord(num1[i]) - ord('0') if i>=0 else 0
            k2 = ord(num2[j]) - ord('0') if j>=0 else 0
            val = k1 + k2 + carry
            res.append(val % 10)
            carry = val // 10

            i-=1
            j-=1

        if carry == 1:
            res.append(1)
        return ''.join(str(x) for x in res[::-1])