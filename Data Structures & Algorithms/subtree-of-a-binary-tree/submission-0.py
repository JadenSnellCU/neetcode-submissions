# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root,subRoot):
            if root is None and subRoot is None:
                return True
            elif (root is not None and subRoot is None) or (root is None and subRoot is not None):
                return False
            elif root.val == subRoot.val:
                sl = sameTree(root.left,subRoot.left)
                sr = sameTree(root.right,subRoot.right)
                return sl and sr
            else:
                return False
        def dfs(node,subRoot):
            if node is None:
                return False
            same = sameTree(node,subRoot)
            l =dfs(node.left,subRoot)
            r=dfs(node.right,subRoot)
            return same or l or r
        return dfs(root,subRoot)
