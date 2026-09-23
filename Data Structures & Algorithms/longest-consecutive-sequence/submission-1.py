class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                counter = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    counter += 1
                if counter > res:
                    res = counter
        return res