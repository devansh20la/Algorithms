# Two Sum Problem https://leetcode.com/problems/two-sum/
from typing import List

# Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]

# Hash Maps
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i in range(len(nums)):
            if target - nums[i] in maps:
                return [i, maps[target - nums[i]]]
            else:
                maps[nums[i]] = i
