'''
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        ret = []
        if root == None:
            return ret
        if root.left != None:
            ret += self.inorderTraversal(root.left)
        ret.append(root.val)
        if root.right != None:
            ret += self.inorderTraversal(root.right)
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