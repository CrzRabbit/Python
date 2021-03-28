from leetcode.tools.tree import *
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                temp = root.left
                while temp and temp.right != root:
                    temp = temp.right
                if temp is None:
                    temp.right = root
                    root = root.left
                else:
                    root = root.right
                    temp.right = None
            else:
                root = root.right

n0 = TreeNode(0)
n1 = TreeNode(1)
n0.left = n1
n2 = TreeNode(2)
n0.right = n2
n3 = TreeNode(3)
n2.left = n3

so = Solution()
showTree(n0)
morrisTraverse(n0)
recoverTree(n0)
morrisTraverse(n0)
so.recoverTree(n0)
showTree(n0)