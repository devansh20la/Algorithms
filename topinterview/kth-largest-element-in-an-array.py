class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_list = []
        
        for i in nums:
            heapq.heappush(heap_list, i)
            
            if len(heap_list) > k:
                heapq.heappop(heap_list)
            
        
        return heapq.heappop(heap_list)