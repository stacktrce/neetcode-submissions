class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        best, curr = -math.inf,0

        for i in range(len(nums)):

            if ((curr + nums[i]) < nums[i]):
                curr = nums[i]
            
            else:
                curr += nums[i]
            
            best = max(best, curr)
            
        return best
