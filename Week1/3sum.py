# 3sum
# url https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        if len(nums) < 3:
            return []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]
            j = i + 1
            k = len(nums) - 1

            while (j < k):
                if nums[j] + nums[k] == -target:
                    res.append([target, nums[j], nums[k]])
                    # find all possible cases with this particular nums[i] 
                    # this is done so that I dont have to repeat is again and do line 15-16
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1

                elif nums[j] + nums[k] < -target:
                    j += 1
                elif nums[j] + nums[k] > -target:
                    k -= 1

        return res


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))