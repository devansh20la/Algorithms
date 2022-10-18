# jump game
# https://leetcode.com/problems/jump-game
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            return True

        left_most_good = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= left_most_good:
                left_most_good = i
        
        return left_most_good == 0