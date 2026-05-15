class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        res = 0
        while num >= 10:
            rem = num % 10
            res = res*10 + rem
            num = num // 10
        
        if num > 0:
            res = res*10 + num
        
        if x < 0:
            res = -res
        
        if -2**31 <= res <= 2**31 - 1:
            return res
        
        return 0