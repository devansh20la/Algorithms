class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        results = []
        for idx, digit in enumerate(num1):
            temp = ["0"]*idx + self.multiply_single_digit(num2, digit)
            results.append(temp) # reverse each 
                
        return self.add_results(results)
        
    
    def multiply_single_digit(self, num, digit1):
        
        result = []
        carry = 0
        for digit2 in num:
            ans = int(digit1) * int(digit2) + carry
            carry = ans // 10
            result.append(str(ans % 10))
        
        if carry > 0:
            result.append(str(carry))
        
        return result
    
    def add_results(self, results):
        sum_total = results[0]
        
        for value in results[1:]:
            
            if len(value) < len(sum_total):
                value = value + ["0"]*(len(sum_total) - len(value))
            elif len(value) > len(sum_total):
                sum_total = sum_total + [0]*(-len(sum_total) + len(value))
            
            assert len(sum_total) == len(value)
                        
            carry = 0
            for i in range(len(value)):
                ans = int(sum_total[i]) + int(value[i]) + carry
                sum_total[i] = str(ans % 10)
                carry = ans // 10
            
            if carry > 0:
                sum_total.append(str(carry))
                
        return "".join(sum_total[::-1])