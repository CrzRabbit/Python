from leetcode.tools.tree import *
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def buildTree(left, right):
            if left > right:
                return None
            index = (left + right + 1) // 2
            root = TreeNode(nums[index])
            root.left = buildTree(left, index - 1)
            root.right = buildTree(index + 1, right)
            return root
        return buildTree(0, nums.__len__() - 1)

so = Solution()
showTree(so.sortedArrayToBST([-11, -10, -3, 0, 5, 9, 10, 11, 12, 13, 14, 15, 16]), 3)