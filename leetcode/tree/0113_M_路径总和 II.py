from leetcode.tools.tree import *
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        ret = []
        def getPath(root, targetSum, temp):
            if not root:
                return
            temp.append(root.val)
            if not root.left and not root.right and root.val == targetSum:
                t = []
                for p in temp:
                    t.append(p)
                ret.append(t)
                return temp[:-1]
            if root.left:
                temp = getPath(root.left, targetSum - root.val, temp)
            if root.right:
                temp = getPath(root.right, targetSum - root.val, temp)
            return temp[:-1]
        getPath(root, targetSum, [])
        return ret

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
n1.right = n5
n6 = TreeNode(6)
n2.right = n6
n7 = TreeNode(2)
n5.right = n7
so = Solution()
showTree(n0)
so = Solution()
print(so.pathSum(n0, 8))