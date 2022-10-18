class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        d1 = []
        i = 0
        while(i < len(seats)):
            if seats[i] == 1:
                d1.append(0)
            else:
                if len(d1) > 0:
                    d1.append(d1[-1] + 1)
                else:
                    d1.append(float('inf'))
            i+=1
        
        d2 = []
        i = len(seats) - 1
        while(i > -1):
            if seats[i] == 1:
                d2.append(0)
            else:
                if len(d2) > 0:
                    d2.append(d2[-1] + 1)
                else:
                    d2.append(float('inf'))
            i-=1
        d2 = d2[::-1]
        
        d = [min(x,y) for x, y in zip(d1,d2)]
        return max(d)