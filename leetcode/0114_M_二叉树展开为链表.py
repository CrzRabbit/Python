from leetcode.tools.tree import *
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        def getFlatten(root):
            if not root:
                return None
            if not root.left and not root.right:
                return root
            elif root.left and root.right:
                t1 = root.right
                root.right = root.left
                t2 = getFlatten(root.left)
                t2.right = t1
                root.left = None
                return getFlatten(t1)
            elif root.left and not root.right:
                root.right = root.left
                root.left = None
                return getFlatten(root.right)
            elif root.right and not root.left:
                return getFlatten(root.right)
            return root
        getFlatten(root)

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
n1.right = n5
n6 = TreeNode(6)
n2.right = n6
n7 = TreeNode(2)
n5.right = n7
so = Solution()
showTree(n0)
so = Solution()
so.flatten(n0)
showTree(n0)