class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        subsets = []

        def backtrack(index):

            if index >= len(nums):
                res.append(subsets.copy())
                return 
            
            subsets.append(nums[index])
            backtrack(index + 1)

            subsets.pop()
            backtrack(index + 1)


        backtrack(0) #dfs algorithm
        return res



        
