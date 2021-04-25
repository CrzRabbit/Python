'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
'''
from leetcode.tools.tree import *
class Solution:
    def numTrees(self, n: int) -> int:
        table = dict()
        def genTree(x, y):
            nodes = []
            if x == y:
                node = TreeNode(x)
                nodes.append(node)
                return 1
            if x > y:
                nodes.append(None)
                return 1
            count = 0
            for i in range(x, y + 1):
                if table.keys().__contains__(i - x):
                    left_trees = table[i - x]
                else:
                    left_trees = genTree(x, i - 1)
                    table[i - x] = left_trees
                if table.keys().__contains__(y - i):
                    right_trees = table[y - i]
                else:
                    right_trees = genTree(i + 1, y)
                    table[y - i] = right_trees
                count += left_trees * right_trees
            return count
        return genTree(1, n)

so = Solution()
print(so.numTrees(10))