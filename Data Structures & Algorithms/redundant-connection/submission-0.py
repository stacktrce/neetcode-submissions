class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        adjL = [[] for _ in range(n + 1)]



        def dfs(node, parent, visited):


            if node in visited:
                return True

            visited.add(node)

            for adj in adjL[node]:

                if adj == parent:
                    continue
                
                if dfs(adj, node, visited):
                    return True
            
            return False
        

        

        for a,b in edges:
            adjL[a].append(b)
            adjL[b].append(a)

            if dfs(a, -1, set()):
                return [a,b]
           

            