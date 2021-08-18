from leetcode.tools.tree import *
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0
        if not root or (not root.left and not root.right):
            return 0
        def getCountPairs(root):
            temp = 0
            if not root:
                return [], 0
            if not root.left and not root.right:
                return [1], 0
            else:
                left_leafs, left_counts = getCountPairs(root.left)
                right_leafs, right_counts = getCountPairs(root.right)
                temp += left_counts
                temp += right_counts
                for l in left_leafs:
                    for r in right_leafs:
                        if l + r <= distance:
                            temp += 1
                leafs = []
                for leaf in left_leafs:
                    leafs.append(leaf + 1)
                for leaf in right_leafs:
                    leafs.append(leaf + 1)
                return leafs, temp
        l, count = getCountPairs(root)
        return count

n0 = constructMaximumBinaryTree([5, 2, 4, 6, 1, 10, 2, 7, 1])
showTree(n0)
so = Solution()
print(so.countPairs(n0, 4))