"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []
        stack = [root]
        if root is None:
            return []
        while stack:
            tmp_root = stack.pop()
            if not tmp_root is None:
                output.append(tmp_root.val)
            for tmp_children in tmp_root.children:
                if not tmp_children is None:
                    stack.append(tmp_children)
        return output[::-1]