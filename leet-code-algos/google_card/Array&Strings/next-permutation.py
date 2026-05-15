class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            k = len(nums)-1
            while(k > 0 and nums[k-1] >= nums[k]):
                k-=1

            if k == 0:
                nums.sort()
            else:
                k-=1
                i = k + 1
                while(i < len(nums) and nums[i] > nums[k]):
                    i+=1
                i-=1
                nums[k], nums[i] = nums[i], nums[k]
                nums[k+1:] = nums[k+1:][::-1]
        
        