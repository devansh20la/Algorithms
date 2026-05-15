class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        used = set()
        used.add(0)
        cross = collections.Counter({
            (1,3):2,
            (3,1):2,
            (1,7):4,
            (7,1):4,
            (3,9):6,
            (9,3):6,
            (7,9):8,
            (9,7):8,
            (1,9):5,
            (9,1):5,
            (2,8):5,
            (8,2):5,
            (3,7):5,
            (7,3):5,
            (4,6):5,
            (6,4):5
        })
                        
        def dfs(i, k):
            ans = 0
            if k == 0:
                return 1
            
            used.add(i)
            for p in range(1, 10):
                if p not in used and cross[i,p] in used:
                    ans += dfs(p, k-1)
            used.remove(i)
            
            return ans     
        
        return sum(4*dfs(1, k) + 4*dfs(2, k) + dfs(5, k) for k in range(m-1, n))
    