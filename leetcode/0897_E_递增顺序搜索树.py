'''
给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。

示例 1：
输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

示例 2：
输入：root = [5,1,7]
输出：[1,null,5,null,7]

提示：
树中节点数的取值范围是 [1, 100]
0 <= Node.val <= 1000
'''
from leetcode.tools.tree import *
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ret = None
        tr = None
        while root:
            if root.left:
                temp = root.left
                while temp.right != None and temp.right != root:
                    temp = temp.right
                if temp.right == root:
                    root.left = None
                    tr.right = root
                    tr = root
                    root = root.right
                else:
                    temp.right = root
                    root = root.left
            else:
                if not ret:
                    ret = root
                    tr = root
                else:
                    tr.right = root
                    tr = root
                root = root.right
        return ret

so = Solution()
n0 = TreeNode(0)
n1 = TreeNode(1)
n0.left = n1
n2 = TreeNode(2)
n0.right = n2
n3 = TreeNode(3)
n2.left = n3
n4 = TreeNode(4)
n3.left = n4
n5 = TreeNode(5)
# n1.right = n5
n6 = TreeNode(6)
n2.right = n6
so = Solution()
showTree(n0)
showTree(so.increasingBST(n0))