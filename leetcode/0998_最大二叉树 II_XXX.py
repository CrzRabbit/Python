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

    def insertIntoMaxTree(self, root: TreeNode, val: int):
        node = TreeNode(val)
        if not root or val > root.val:
            node.left = root
            return node
        elif root.right and val > root.right.val:
            node.left = root.right
            root.right = node
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
        return root

so = Solution()
n0 = so.constructMaximumBinaryTree([5,2,4, 6, 1, 10, 2, 7, 1])
showTree(n0)
showTree(so.insertIntoMaxTree(n0, 3))