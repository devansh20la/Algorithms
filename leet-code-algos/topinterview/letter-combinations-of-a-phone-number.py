class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        bible = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        
        if len(digits) == 0:
            return []

        res = []
        def backtrack(digit_index, path):
            
            if digit_index == len(digits):
                res.append(path)
                return

            possible_letters = bible[digits[digit_index]]
            
            for letter in possible_letters:
                backtrack(digit_index+1, path + letter)
        
        backtrack(0, "")
        return res