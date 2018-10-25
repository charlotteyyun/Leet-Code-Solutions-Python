"""
Given a binary tree, return the postorder traversal of its nodes' values.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        if root is None:
            return []
        s1 = [root]
        trans = []
        while s1:
            r= s1.pop()
            trans.append(r.val)
            if r.left:
                s1.append(r.left)
            if r.right:
                s1.append(r.right)
        trans.reverse()
        return trans
        """
        :type root: TreeNode
        :rtype: List[int]
        """