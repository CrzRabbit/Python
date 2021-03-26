from leetcode.tools.tree import *
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        if (root.left and self.hasPathSum(root.left, targetSum - root.val)) \
            or (root.right and self.hasPathSum(root.right, targetSum - root.val)):
            return True
        return False

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
so = Solution()
print(so.hasPathSum(n0, 9))