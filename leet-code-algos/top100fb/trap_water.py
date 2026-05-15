# Trapping rain water
# https://leetcode.com/problems/trapping-rain-water

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]*len(height)
        right_max = [0]*len(height)
    
        if len(height) == 0:
            return 0
    
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            right_max[i] = max(height[i], right_max[i+1])
        
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])
        
        print(left_max, right_max)
        water = 0
        for i in range(len(height)):
            water += min(left_max[i], right_max[i]) - height[i]
            
        return water