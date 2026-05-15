class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        smallest = float('inf')
        points_set = set((p[0], p[1]) for p in points)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]

                if x1 < x2 and y1 < y2 and x1 != x2 and y1 != y2 and (x1, y2) in points_set and (x2, y1) in points_set:
                    smallest = min((x2 - x1) * (y2 - y1), smallest)
                
        return smallest if smallest != float('inf') else 0

