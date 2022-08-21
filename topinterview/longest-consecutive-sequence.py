class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        longest_streak = 0
        for num in nums:
            if num - 1 not in nums:
                curr_streak = 1
                
                while num + 1 in nums:
                    curr_streak += 1
                    num += 1

                longest_streak = max(longest_streak, curr_streak)
        
        return longest_streak