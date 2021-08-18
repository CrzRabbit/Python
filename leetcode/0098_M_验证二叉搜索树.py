'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
'''
from leetcode.tools.tree import *
class Solution:
    def isValidBST(self, root):
        def inorderTraversal(root: TreeNode):
            ret = []
            left_ret = []
            right_ret = []
            if root == None:
                return ret, True
            left_valid = True
            right_valid = True
            if root.left != None:
                left_ret, left_valid = inorderTraversal(root.left)
            ret += left_ret
            ret.append(root.val)
            if root.right != None:
                right_ret, right_valid = inorderTraversal(root.right)
            ret += right_ret
            valid = left_valid and right_valid
            if left_ret.__len__() and left_ret[left_ret.__len__() - 1] >= root.val:
                valid = valid and False
            if right_ret.__len__() and right_ret[0] <= root.val:
                valid = valid and False
            return ret, valid
        nodes, valid = inorderTraversal(root)
        return valid

n0 = TreeNode(0)
n1 = TreeNode(1)
n0.right = n1
n2 = TreeNode(2)
n0.left = n2
n3 = TreeNode(3)
n2.right = n3

so = Solution()
print(so.isValidBST(n0))