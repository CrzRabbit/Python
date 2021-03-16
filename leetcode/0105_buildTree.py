from leetcode.tools.tree import *
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:

so = Solution()
showTree(so.buildTree([3,9,20,15,7], [9,3,15,20,7]))