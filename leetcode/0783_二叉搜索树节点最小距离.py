'''
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
'''
from leetcode.tools.tree import *
class Solution:
    '''
    前序遍历，然后依次比较
    '''
    def minDiffInBST(self, root: TreeNode) -> int:
        nodes = []
        def getNodes(root):
            if not root:
                return
            if root.left:
                getNodes(root.left)
            nodes.append(root.val)
            if root.right:
                getNodes(root.right)
        getNodes(root)
        min = 10 ** 5
        for i in range(len(nodes) - 1):
            temp = nodes[i + 1] - nodes[i]
            if temp < min:
                min = temp
        return min
    '''
    morris 遍历，然后依次比较
    '''
    def _minDiffInBST(self, root: TreeNode) -> int:
        min = 10 ** 5
        temp = None
        while root:
            if root.left:
                node = root.left
                while node.right and node.right != root:
                    node = node.right
                if node.right:
                    node.right = None
                    if temp:
                        if root.val - temp < min:
                            min = root.val - temp
                    temp = root.val
                    root = root.right
                else:
                    node.right = root
                    root = root.left
            else:
                if temp:
                    if root.val - temp < min:
                        min = root.val - temp
                temp = root.val
                root = root.right
        return min

nums = [1, 3, 11, 44, 59, 123]
so = Solution()
print(so.minDiffInBST(constructMaximumBinaryTree(nums)))
print(so._minDiffInBST(constructMaximumBinaryTree(nums)))