# find first and last position of sorted array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        while (l <= r):
            M = (l + r) // 2
            if nums[l] == nums[r] == target:
                return [l, r]
            if nums[M] < target:
                l = M+1
            elif nums[M] > target:
                r = M-1
            else:
                if nums[l] != target:
                    l += 1

                if nums[r] != target:
                    r -= 1
        return [-1, -1]
