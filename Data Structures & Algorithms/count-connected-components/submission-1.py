class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = {c: [] for c in range(n)}

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        

        visited = set()

        def dfs(node):
            
            if node in visited:             
                return

            visited.add(node)

            for adj in adjList[node]:
                
                dfs(adj)
                    
        res = 0

        for node in range(n):
            if not (node in visited):
                dfs(node)
                res += 1
        return res
        



