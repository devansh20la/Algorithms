class Solution:
    def nextClosestTime(self, time: str) -> str:
        nums = time.replace(":","")
        res = []
        for i in range(len(nums)):
            num = nums[i]
            if num not in res:
                res.append(int(num))
        
        all_comb = []
        for i in res:
            for j in res:
                all_comb.append(i*10 + j)
        all_comb = sorted(all_comb)
        
        
        mm = int(time.split(":")[1])
        n_mm = all_comb[0]
        for i in all_comb:
            if mm < i < 60 :
                n_mm = i
                break
        
        hh = int(time.split(":")[0])
        if n_mm == all_comb[0]:
            n_hh = all_comb[0]
            for i in all_comb:
                if hh < i < 24 :
                    n_hh = i
                    break
        else:
            n_hh = hh
        
        return "{:02d}:{:02d}".format(n_hh,n_mm)
        