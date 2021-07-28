'''
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。


示例 1：

输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。

示例 2：

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3


提示:

二叉树的节点个数的范围是 [0,1000]
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
'''
from leetcode.tools.time import printTime
from leetcode.tools.tree import TreeNode, buildTree, showTree


class Solution:
    '''
    前缀和 + 回溯
    '''
    @printTime()
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        showTree(root, 2)
        if root == None:
            return 0
        mem = {0: 1}
        table = []
        state = []
        cur = root
        sum = 0
        ret = 0
        while cur:
            sum += cur.val
            if sum - targetSum in mem:
                ret += mem[sum - targetSum]
            if cur.left:
                table.append(cur)
                state.append(0)
                cur = cur.left
                if sum not in mem:
                    mem[sum] = 0
                mem[sum] += 1
            elif cur.right:
                table.append(cur)
                state.append(1)
                cur = cur.right
                if sum not in mem:
                    mem[sum] = 0
                mem[sum] += 1
            else:
                sum -= cur.val
                cur = None
                while state.__len__() > 0 and (state[-1] == 1 or table[-1].right == None):
                    mem[sum] -= 1
                    sum -= table[-1].val
                    table = table[:-1]
                    state = state[:-1]
                if state.__len__() and state[-1] == 0:
                    state[-1] = 1
                    cur = table[-1].right
        return ret

root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
targetSum = 22
Solution().pathSum(buildTree(root), targetSum)