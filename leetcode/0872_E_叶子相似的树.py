'''
请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
'''
from leetcode.tools.tree import *


class Solution:
    '''
    深度优先遍历
    '''
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeaf(node):
            leaf = []
            if not node:
                return leaf
            if node.left:
                leaf += getLeaf(node.left)
            if node.right:
                leaf += getLeaf(node.right)
            if not node.left and not node.right:
                leaf.append(node.val)
            return leaf
        return getLeaf(root1) == getLeaf(root2)


root1 = buildTree([3,5,1,6,2,9,8,None,None,7,4])
showTree(root1)
root2 = buildTree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
showTree(root2)
so = Solution()
print(so.leafSimilar(root1, root2))