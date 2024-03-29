'''
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。



示例 1：

输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：

输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

提示：

树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.val <= 1000
'''
from leetcode.tools.time import printTime
from leetcode.tools.tree import TreeNode, buildLTree


class Solution:
    @printTime()
    def maxPathSum(self, root: TreeNode) -> int:
        self.ret = root.val
        def recursion(node):
            t, tl, tr = 0, 0, 0
            if node.left is None and node.right is None:
                t = node.val
            else:
                if node.left:
                    tl = recursion(node.left)
                if node.right:
                    tr = recursion(node.right)
                t = max(node.val, node.val + tl, node.val + tr, node.val + tl + tr)
            self.ret = max(self.ret, t)
            return max(node.val, node.val + tl, node.val + tr)
        recursion(root)
        return self.ret

root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
Solution().maxPathSum(buildLTree(root))