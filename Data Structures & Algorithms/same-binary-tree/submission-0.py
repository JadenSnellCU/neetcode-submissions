# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (p is not None and q is None):
            return False
        elif p.val==q.val:
            sl = self.isSameTree(p.left,q.left)
            sr = self.isSameTree(p.right,q.right)
            return (sl and sr)
        else:
            return False
        