from leetcode.tools.tree import *
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        pass

n0 = constructMaximumBinaryTree([5, 2, 4, 6, 1, 10, 2, 7, 1])
showTree(n0)
n1 = constructMaximumBinaryTree([2, 7, 1])
showTree(n1)
so = Solution()
print(so.isSubStructure(n0, n1))