class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = collections.defaultdict(set)
        seen_colums = collections.defaultdict(set)
        seen_squares = collections.defaultdict(set)

        l = len(board)
        counter = 0

        for n in range(l):
            for n2 in range(l):
                val = board[n][n2]
                if (board[n][n2] == "."): 
                    continue
                    
                if (val in seen_rows[n] or val in seen_colums[n2] or val in seen_squares[(n // 3, n2 //3)]):
                    return False

                seen_rows[n].add(val)
                seen_colums[n2].add(val)
                seen_squares[(n // 3, n2 //3)].add(val)
        
        return True
