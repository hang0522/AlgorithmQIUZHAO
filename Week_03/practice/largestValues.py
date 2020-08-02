# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.result =[]
        queue =collections.deque()
        queue.append(root)
        while queue:
            #curr_max = float('-inf') 
            cur_layer = []           
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                cur_layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #print(cur_layer)
            if cur_layer:
                #print(max(cur_layer))
                self.result.append(max(cur_layer))
        return self.result