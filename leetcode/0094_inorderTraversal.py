# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        nodes = []
        ret = []
        if root == None:
            return ret
        if root.left != None:
            nodes.append(root)
        elif root.right != None:
            ret.append(root.val)
            nodes.append(root.right)
        else:
            ret.append(root.val)
            return ret
        while nodes.__len__():
            temp = nodes[nodes.__len__() - 1]
            nodes = nodes[:nodes.__len__() - 1]
            print(temp.val)
            if temp.left != None:
                t1 = temp.left
                temp.left = None
                nodes.append(temp)
                nodes.append(t1)
            elif temp.right != None:
                ret.append(temp.val)
                nodes.append(temp.right)
            else:
                ret.append(temp.val)
        return ret

n0 = TreeNode(0)
n1 = TreeNode(1)
n0.right = n1
n2 = TreeNode(2)
n0.left = n2
n3 = TreeNode(3)
n2.right = n3

so = Solution()
print(so.inorderTraversal(n0))