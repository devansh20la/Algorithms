# sort colors
# https://leetcode.com/problems/sort-colors/

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 # left boundary
        r = len(nums) - 1 # right boundary
        i = 0 # index

        while (i <= r):
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            elif nums[i] == 1:
                i += 1