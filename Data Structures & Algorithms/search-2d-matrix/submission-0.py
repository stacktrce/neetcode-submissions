class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in matrix:
            l,h = 0 , len(i)-1

            while l <= h: 

                mid = (l + h) // 2

                if (i[mid] == target):
                    return True

                elif (i[mid] > target): 
                    h = mid -1

                else: l = mid+1

        return False


