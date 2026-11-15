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

        # Merkt sich: { original_node : geklonter_node }
        old_to_new = {}
        old_to_new[node] = Node(node.val)

        q = collections.deque([node])

        while q:
            curr = q.popleft()

            for neighbor in curr.neighbors:
                # 1. Wenn der Nachbar noch nie geklont wurde:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)  # Nur unbesuchte Knoten in die Queue!

                # 2. Den geklonten Nachbarn an den geklonten aktuellen Knoten anhängen:
                old_to_new[curr].neighbors.append(old_to_new[neighbor])

        # Gib den Klon des Startknotens zurück
        return old_to_new[node]

        