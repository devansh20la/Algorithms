# Remove duplicates
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    	i = 0
    	j = 0
    	while(j < len(nums)):
    		if nums[i] == nums[j]:
    			j += 1
	    	else:
	    		nums[i+1], nums[j] = nums[j], nums[i+1]
	    		i += 1
	    		j += 1
    	return nums[0:i+1], i


s = Solution()
print(s.removeDuplicates([1,1,2]))