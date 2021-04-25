# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node'):
        ret = []
        def getPreorder(root):
            if not root:
                return
            ret.append(root.val)
            for node in root.children:
                getPreorder(node)
        getPreorder(root)
        return ret