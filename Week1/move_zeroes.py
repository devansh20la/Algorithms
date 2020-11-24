# move zeros 
# https://leetcode.com/problems/move-zeroes/

from typing import List


def moveZeroes(nums: List[int]) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	j = 0
	for i in range(len(nums)):
		if nums[i] == 0:
			for j in range(i+1, len(nums)):
				if nums[j] != 0:
					nums[i], nums[j] = nums[j], nums[i]
					break
		if j == len(nums) - 1:
			break
		

moveZeroes([1,2,3])
