"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Note:

Both of the given trees will have between 1 and 100 nodes.
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        S1 = [root1]
        S2 = [root2]
        leaf1 = []
        leaf2 = []
        while S1:
            node1 = S1.pop()
            if node1.left:
                S1.append(node1.left)
            if node1.right:
                S1.append(node1.right)
            if not node1.left and not node1.right:
                leaf1.append(node1.val)
        while S2:
            node2 = S2.pop()
            if node2.left:
                S2.append(node2.left)
            if node2.right:
                S2.append(node2.right)
            if not node2.left and not node2.right:
                leaf2.append(node2.val)

        if leaf1[::-1] == leaf2[::-1]:
            return True
        else:
            return False