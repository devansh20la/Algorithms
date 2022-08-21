class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        
        while(start <= end):
            
            mid = (start + end) // 2
            
            if target == nums[mid]:
                return mid

            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
    
            elif nums[mid] < nums[end]:
                if nums[end] >= target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            
        return -1