class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        counter = 0

        def bfs(r, c):

            q = collections.deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    counter += 1
        
        return counter
