# subarray sum equal k
# very tricky
# https://leetcode.com/problems/subarray-sum-equals-k

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        has_map = {0: 1 }
        add = 0
        count = 0
        for i in nums:
            add += i
            if add- k in has_map:
                count += has_map[add-k]
            
            if add in has_map:
                has_map[add] += 1
            else:
                has_map[add] = 1
            
        return count
        