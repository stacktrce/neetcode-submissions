class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        fresh = 0
        q = collections.deque()

        # Erst komplett zählen und alle Start-2er sammeln
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # Danach einmalig BFS für alle gleichzeitig starten
        while q and fresh > 0:
            for i in range(len(q)):
                qRow, qCol = q.popleft()

                for dR, dC in directions:
                    nR, nC = qRow + dR, qCol + dC

                    if (
                        nR < 0
                        or nC < 0
                        or nR >= ROWS
                        or nC >= COLS
                        or grid[nR][nC] == 2  # <- nR, nC statt r, c!
                        or grid[nR][nC] == 0  # <- nR, nC statt r, c!
                    ):
                        continue

                    grid[nR][nC] = 2
                    q.append((nR, nC))
                    fresh -= 1
            
            time += 1  # <- Auf gleicher Höhe wie "for i in range(len(q)):"

        return time if fresh == 0 else -1