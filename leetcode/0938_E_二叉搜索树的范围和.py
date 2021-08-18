'''
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
'''
from leetcode.tools.tree import *
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ret = 0
        while root:
            if root.left:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right
                if temp.right == root:
                    temp.right = None
                    if root.val >= low and root.val <= high:
                        ret += root.val
                    root = root.right
                else:
                    temp.right = root
                    root = root.left
            else:
                if root.val >= low and root.val <= high:
                    ret += root.val
                root = root.right
        return ret

nums = [1, 2, 3, 4, 5, 6, 7]
so = Solution()
print(so.rangeSumBST(sortedArrayToBST(nums), 3, 6))