"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        counter,s,e,res = 0,0,0,0
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        for x in range(len(intervals)):
            if starts[s] < ends[e]:
                s+=1
                counter+=1

            else:
                e += 1
                counter -=1

            res = max(res,counter) 

        return res           







    
        