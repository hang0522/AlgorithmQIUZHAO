"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return root
        output = []
        #queue = [root]
        queue = collections.deque([root])
        while queue:
             output.append([])
             for cnt in range(len(queue)):
                 cur = queue.popleft()
                 if cur:
                     output[-1].append(cur.val)
                 for child in cur.children:
                     queue.append(child)
        return output