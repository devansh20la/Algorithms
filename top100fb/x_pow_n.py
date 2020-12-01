#pow of x
#https://leetcode.com/problems/powx-n


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0.0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        if n == 1.0:
            return x
        print(x, n)
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        return half * half * x