# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # #BFS
        # #valid?
        # if root==None:
        #     return []
        
        # if root.val==None:
        #     return []
        
        # #self.output = [[root.val]]
        # #put visited 
        # self.output = []
        # #put node to be visied
        # queue =collections.deque()
        # queue.append(root)
        # while queue:
        #     size = len(queue)
        #     cur_level = []
        #     for i in range(size):
        #         node = queue.popleft()
                
        #         cur_level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     #queue.append(next_level)
        #     if cur_level:
        #         self.output.append(cur_level)
        # return self.output
        #DFS
        if not root:
            return []
        self.result = [[]]
        #self.result = []
        def DFS(cur,level=0):
            if len(self.result)<=level:
                self.result.append([])
            self.result[level].append(cur.val)
            if cur.left:
                DFS(cur.left,level+1)
            if cur.right:
                DFS(cur.right,level+1)
        DFS(root,0)
        return self.result