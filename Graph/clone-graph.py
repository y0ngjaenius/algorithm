# link: https://leetcode.com/problems/clone-graph

from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        q, dic = deque([node]), {node.val: Node(val=node.val)}
        while q:
            u = q.popleft()
            for v in u.neighbors:
                if v.val not in dic:
                    q.append(v)
                    dic[v.val] = Node(val=v.val)
                dic[u.val].neighbors.append(dic[v.val])
                    
        return dic[node.val]
