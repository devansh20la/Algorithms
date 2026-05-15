from collections import Counter

class Solution:   
    def totalFruit(self, fruits: List[int]) -> int:
        hash_map, l, r, max_length = collections.Counter(), 0, 0, 0
        
        while (r < len(fruits)):
            hash_map[fruits[r]] += 1
            
            while( len(hash_map) > 2 ):
                hash_map[fruits[l]] -= 1
                if not hash_map[fruits[l]]:
                    hash_map.pop(fruits[l])
                l += 1
            
            max_length = max(max_length, r - l + 1)
            r += 1
            
        return max_length