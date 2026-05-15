def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])
    
    rooms = 0
    i = 0
    j = 0
    while i<len(intervals):
        if start_times[i] <= end_times[j]:
            rooms += 1
            i++         
        else:
            j++
        
    return rooms