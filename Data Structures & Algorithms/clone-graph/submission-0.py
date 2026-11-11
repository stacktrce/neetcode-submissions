"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        oldToNew = {}
        


        def bfs(node):

            queue = collections.deque()
            queue.append(node)

            while queue:
                node = queue.popleft()
                
                for n in node.neighbors:
                    if n not in oldToNew:
                        oldToNew[n] = Node(n.val)
                        queue.append(n)
                    oldToNew[node].neighbors.append(oldToNew[n])   
                    
        oldToNew[node] = Node(node.val)
        bfs(node)
        return oldToNew[node]
                


            




            