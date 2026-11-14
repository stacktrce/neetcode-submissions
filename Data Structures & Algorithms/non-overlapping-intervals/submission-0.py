class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])

        res = []
        counter = 0

        res.append(intervals[0])

       

        for i in range(1, len(intervals)):

            if (res[-1][1] > intervals[i][0]):
                counter += 1
            else:
                res.append(intervals[i])
        
        print(res)
        return counter