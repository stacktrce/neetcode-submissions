class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        res = 0

        def bfs(r, c):

            q = collections.deque()
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                qRow, qCol = q.popleft()


                for dR, dC in directions:
                    nR, nC = qRow + dR, qCol + dC

                    if nR < 0 or nC < 0 or nR >= rows or nC >= cols or grid[nR][nC] == "0":
                        continue
                    q.append((nR, nC))
                    grid[nR][nC] = "0"
                    

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1"):
                    bfs(r,c)
                    res += 1
        return res
