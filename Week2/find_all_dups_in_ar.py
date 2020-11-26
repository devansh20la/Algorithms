# find all duplicates in an array
# https://leetcode.com/problems/find-all-duplicates-in-an-array

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        out = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                out.append(index + 1)
            else:
                nums[index] = -nums[index]
        return out