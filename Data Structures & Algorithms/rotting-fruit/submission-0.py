class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]

        def bfs():

            nonlocal minutes
            nonlocal counter

            while q:
                qrow, qcol, minutes = q.popleft()
                grid[qrow][qcol] = 2

                for dRow, dCol in directions:
                    nr, nc = qrow + dRow, qcol + dCol
                    if (
                        nr < 0
                        or nc < 0
                        or nr >= rows
                        or nc >= cols
                        or not grid[nr][nc] == 1
                        or grid[nr][nc] == 2
                        or (nr, nc) in visited
                    ):
                        continue
                    q.append((nr, nc, minutes + 1))
                    counter -= 1
                    visited.add((nr, nc))

        q = collections.deque()
        visited = set()
        minutes = 0
        counter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    counter += 1
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    visited.add((r, c))

        bfs()
        if counter == 0:
            return minutes
        else:
            return -1
