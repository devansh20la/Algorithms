# Container with most water 
# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxarea = -1.0
        while (i < j):
            if (j - i)*min(height[i], height[j]) > maxarea:
                maxarea = (j - i)*min(height[i], height[j])
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxarea