class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        output = [1] * length

        prefix = 1 
        for n in range(length):
            output[n] = prefix
            prefix *= nums[n]

        suffix = 1
        for i in range(length -1, -1 , -1):
            output[i] *= suffix
            suffix *= nums[i]    

        return output 
            

