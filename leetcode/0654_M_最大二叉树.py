from leetcode.tools.tree import *
class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        if nums.__len__() == 0:
            return None
        def getTree(nums, left, right):
            if left == right:
                return None
            index = left
            for i in range(left + 1, right):
                if nums[i] > nums[index]:
                    index = i
            node = TreeNode(nums[index])
            node.left = getTree(nums, left, index)
            node.right = getTree(nums, index + 1, right)
            return node
        return getTree(nums, 0, nums.__len__())

so = Solution()
showTree(so.constructMaximumBinaryTree([3,2,1,6,0,5]))