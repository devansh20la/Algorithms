from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return 0
        jump_arr = [None] * (len(nums) - 1) + [True]
        min_jumps_from_idx = [float('inf')] * (len(nums) - 1) + [0]

        for i in range(len(nums) - 2, -1, -1):
            min_jump = float('inf')

            for j in range(min(i + nums[i], len(nums)-1), i, -1):
                print(i, j, min_jumps_from_idx, jump_arr)
                if jump_arr[j] is True:
                    jump_arr[i] = True
                    if min_jumps_from_idx[j] + 1 < min_jump:
                        min_jump = min_jumps_from_idx[j] + 1
            min_jumps_from_idx[i] = min_jump

        return min_jumps_from_idx[0]


s = Solution()
print(s.canJump([2, 1]))