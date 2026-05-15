class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = [(w/q, w, q) for w,q in zip(wage, quality)]
        workers = sorted(workers, key = lambda y: y[0])
        
        ans = float('inf')
        pool = []
        sumq = 0
        
        for ratio, w, q in workers:
            heapq.heappush(pool, -q)
            sumq += q
            
            if len(pool) > k:
                sumq -= -heapq.heappop(pool)
            
            if len(pool) == k:
                ans = min(ans, ratio*sumq)
        
        return ans
        