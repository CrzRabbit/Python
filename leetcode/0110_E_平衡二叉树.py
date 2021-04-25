from leetcode.tools.tree import *
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def getDepth(node):
            if not node:
                return 0, True
            else:
                left_depth, left_ba = getDepth(node.left)
                right_depth, right_ba = getDepth(node.right)
                flag = True
                if left_depth - right_depth > 1 or left_depth - right_depth < -1 or not left_ba or not right_ba:
                    flag = False
                if left_depth >= right_depth:
                    return left_depth + 1, flag
                else:
                    return right_depth + 1, flag
        left_depth, left_ba = getDepth(root.left)
        right_depth, right_ba = getDepth(root.right)
        if (left_depth - right_depth > 1 or left_depth - right_depth < -1) or not left_ba or not right_ba:
            return False
        else:
            return True

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
#n1.right = n5
n6 = TreeNode(6)
n2.right = n6
so = Solution()
showTree(n0)
so = Solution()
print(so.isBalanced(n0))
