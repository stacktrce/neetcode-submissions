class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low,high = 0, len(nums) -1 

        while low <= high:

            mid = (high+low) // 2

            if (target == nums[mid]):
                return mid

            if (target < nums[mid]):
                high = mid - 1 

            elif (target > nums[mid]): 
                low = mid + 1
        
        return -1