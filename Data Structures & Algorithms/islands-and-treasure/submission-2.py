class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def bfs():
            while q:

                qrow, qcol, dist = q.popleft()

                grid[qrow][qcol] = dist

                for rowDirection, colDirection in directions:
                    nr, nc = qrow + rowDirection, qcol + colDirection
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == -1 or (nr,nc) in visited:
                        continue
                    visited.add((nr,nc))
                    q.append((nr, nc, dist+1))

        q = collections.deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))

        bfs()