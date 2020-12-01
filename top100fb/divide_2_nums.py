# divide two numbers
# https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
    
        # only because this number cannot fit in memory
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        quotient = 0

        if dividend < 0 or divisor < 0:
            neg = True
            if  dividend < 0 and divisor < 0:
                neg = False
        else:
            neg = False
    
        dividend = -abs(dividend)
        divisor = -abs(divisor)
        while(divisor>=dividend):
            p_o_2 = -1
            val = divisor
            
            while (val + val >= dividend):
                val += val
                p_o_2 += p_o_2
                
            quotient += p_o_2
            dividend -= val
            
        if neg:
            return -abs(quotient)
        else:
            return abs(quotient)
        