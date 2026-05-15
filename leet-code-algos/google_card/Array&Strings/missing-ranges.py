class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if len(nums) == 0:
            if lower == upper:
                return ["{}".format(lower)]
            else:
                return ["{}->{}".format(lower, upper)]
        
        if lower == upper:
            return []
        
        p, q = lower, upper
        
        out = []
        for i in nums:
            if p != i:
                if p == i-1:
                    out.append("{}".format(p))
                else:
                    out.append("{}->{}".format(p, i-1))
                    
            p = i+1
        
        if p != q and p<q:
            out.append("{}->{}".format(p,q))
        
        if p == q:
            out.append("{}".format(q))
        
        return out