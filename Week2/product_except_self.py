# prodcut except self
# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        left = [1]
        right = [1]
        while(r > 0):
            if r == len(nums) - 1:
                left.append(nums[l])
                right.append(nums[r])
            else:
                left.append(left[-1] * nums[l])
                right.append(right[-1] * nums[r])

            l += 1
            r -= 1

        return [x*y for x, y in zip(left, right[::-1])]


s = Solution()
print(s.productExceptSelf([1,2,3,4]))