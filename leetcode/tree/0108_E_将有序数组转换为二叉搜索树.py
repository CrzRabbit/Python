'''
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
'''
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