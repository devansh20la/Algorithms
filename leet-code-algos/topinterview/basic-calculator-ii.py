import math 

class Solution:
    def calculate(self, s: str) -> int:
        if s == "":
            return None
        
        s = s.replace(" ", "")
        
        ops = "+"
        a = []
        curr_num = last_num = result = 0
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                curr_num = curr_num*10 + int(char)
            
            if char.isdigit() != True or i == len(s) - 1:
                if ops == "+" or ops == '-':
                    result += last_num
                    last_num = curr_num if ops == "+" else -curr_num
                if ops == "*":
                    last_num = last_num * curr_num
                if ops == "/":
                    last_num = math.floor(last_num / curr_num) if last_num > 0 else math.ceil(last_num / curr_num)
                ops = char
                curr_num = 0
        
        return result+last_num