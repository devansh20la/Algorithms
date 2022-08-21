class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {}
        
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 0
        
        sorted_list = sorted(list(hash_map.keys()), key = lambda x: hash_map[x])
        
        return sorted_list[-k:]

# this is O(Nlog(N)) solution. This can be improved to O(NlogK) using heaps and O(N) using bucket sort idea.