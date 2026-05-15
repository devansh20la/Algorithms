class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        rev_pairs = {
            "0" : "0",
            "1" : "1",
            "6" : "9",
            "8" : "8",
            "9" : "6"
        }
        
        def gen_numbs(n, final_length):
            
            if n == 0:
                return [""]
            
            if n == 1:
                return ["0", "1", "8"]
            
            prev_strob_nums = gen_numbs(n - 2, final_length)
            curr_nums = []
            for key, rev_key in rev_pairs.items():
                for p in prev_strob_nums:
                    if key != "0" or n < final_length:
                        curr_nums.append(key + p + rev_key)
                        
            return curr_nums
        
        return gen_numbs(n, n)