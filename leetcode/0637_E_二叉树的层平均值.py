'''
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
'''
from typing import List

from leetcode.tools.tree import *

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ret = []
        nodes = [root]
        while len(nodes):
            temp = []
            total = 0
            for node in nodes:
                total += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            ret.append(total / len(nodes))
            nodes = temp
        return ret

nums = [3,9,20,None,None,15,7]
showTree(buildTree(nums))
so = Solution()
print(so.averageOfLevels(buildTree(nums)))