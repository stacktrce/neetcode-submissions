class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        #keinen cycle und zusammenhängend = valid tree 

        adjList =  {i: [] for i in range(n)}

        for root,edge in edges:
            adjList[root].append(edge)
            adjList[edge].append(root)
        
        print(adjList)


        visited = set()   
        
        
        def dfs(node,prev):


            if node in visited:
                return False 

            visited.add(node)
            
            for adj in adjList[node]:

                if adj == prev:
                    continue

                if not dfs(adj, node):
                    return False

            return True

        
       
        return dfs(0,-1) and len(visited) == n
        
        
        

            