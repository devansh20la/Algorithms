class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = maxsum = nums[0]
        
        for i in nums[1:]:
            cursum = max(i, cursum + i)
            maxsum = max(maxsum, cursum)
            
        return maxsum
        