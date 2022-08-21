class Solution:
    
    def fastpow(self, x, n):
        if n == 0:
            return 1
        
        half = self.fastpow(x, n // 2)
        
        if (n % 2) == 0:
            return half * half
        else:
            return half * half * x
        
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        
        return self.fastpow(x, n)