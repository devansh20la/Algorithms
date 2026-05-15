#minsubarray
# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ## RC ##
        ## APPROACH : SLIDING WINDOW ##
        ## LOGIC ##
        ## 1. First increase windowsize till sum >= s ##
        ## 2. once you find it, shrink the window size by incrementing the left pointer
        ## 3. when it breaks, continue incrementing the right pointer, (where window start will be left pointer not from index 0)
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##

        windowSum, windowStart = 0, 0
        minLength = math.inf
        for windowEnd in range(len(nums)):
            windowSum+=nums[windowEnd]
            while windowSum >= s:
                minLength = min(minLength, windowEnd - windowStart + 1)
                windowSum -= nums[windowStart]
                windowStart+=1
        if minLength == math.inf:
            return 0
        return minLength