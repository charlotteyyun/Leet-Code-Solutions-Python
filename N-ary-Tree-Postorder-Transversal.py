"""
Given an n-ary tree, return the postorder traversal of its nodes' values.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        if not root:
            return []

        stack, output = [root], []
        while stack:
            r = stack.pop()
            if r:
                output.append(r.val)
            for c in r.children:
                stack.append(c)

        return output[::-1]
        """
        :type root: Node
        :rtype: List[int]
        """
