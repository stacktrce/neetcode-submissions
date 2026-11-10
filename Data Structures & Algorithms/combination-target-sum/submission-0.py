class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        path = []

        s = 0



        def build(i, s):

    
            if s == target:
                res.append(path[:])
                return 

            if i == len(nums):
                return []
        
            if s > target: 
                return
            

            path.append(nums[i])
            build(i, s + nums[i])

            path.pop()
            build(i + 1, s)
        
        build(0, 0)
        return res
            