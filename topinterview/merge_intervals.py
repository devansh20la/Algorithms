class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start = -1
        end = -1
        intervals = sorted(intervals, key= lambda x: x[0])
        output = []
        for interval in intervals:
            
            if start<0 and end<0:
                start = interval[0]
                end = interval[1]
            elif end >= interval[0]:
                end = max(end, interval[1])
            else:
                output += [[start, end]]
                start = interval[0]
                end = interval[1]
        
        output += [[start, end]]
            
        return output
            