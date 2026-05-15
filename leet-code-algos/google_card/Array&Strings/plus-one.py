class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            val = digits[i] + carry
            digits[i] = val % 10
            carry = val // 10
        
        if carry != 0:
            digits = [carry] + digits
        return digits
        