"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node: return None
        clone = {node:Node(node.val)}
        que = deque([node])
        while que:
            cur = que.popleft()
            for n in cur.neighbors:
                if n not in clone:
                    clone[n] = Node(n.val)
                    que.append(n)
                clone[cur].neighbors.append(clone[n])
        return clone[node]
        

        