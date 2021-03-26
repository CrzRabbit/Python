from leetcode.tools.tree import *
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def getMin(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left_depth = getMin(node.left)
            right_depth = getMin(node.right)
            print('===============')
            showTree(node.left)
            print(left_depth)
            showTree(node.right)
            print(right_depth)
            if left_depth <= right_depth:
                if node.left:
                    return left_depth + 1
                else:
                    return right_depth + 1
            else:
                if node.right:
                    return right_depth + 1
                else:
                    return left_depth + 1
        return getMin(root)

n0 = TreeNode(0)
n1 = TreeNode(1)
n0.left = n1
n2 = TreeNode(2)
n0.right = n2
n3 = TreeNode(3)
n2.left = n3
n4 = TreeNode(4)
n3.left = n4
n5 = TreeNode(5)
# n1.right = n5
n6 = TreeNode(6)
n2.right = n6
so = Solution()
showTree(n0)
so = Solution()
print(so.minDepth(n0))
