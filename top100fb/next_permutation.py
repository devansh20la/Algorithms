# next Permutation
# https://leetcode.com/problems/next-permutation
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            for n in range(len(nums) - 1, -1, -1):
                if (n>0):
                    if(nums[n]>nums[n-1]):
                        break
            if n == 0:
                return nums.sort()
            else:
                m = n
                n -=1
                while(m < len(nums) and nums[m] > nums[n]):
                    m+=1

                nums[n], nums[m-1] = nums[m-1], nums[n]
                nums[n+1:] = nums[n+1:][::-1]
            return nums