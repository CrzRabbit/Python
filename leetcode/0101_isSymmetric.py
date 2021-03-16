from leetcode.tools.tree import *
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isNodeSame(p, q):
            if (p and q and p.val == q.val) or (p == None and q == None):
                return True
            return False
        left = []
        right = []
        if root == None:
            return True
        elif isNodeSame(root.left, root.right):
            left.append(root.left)
            right.append(root.right)
        else:
            return False
        while left.__len__() and right.__len__():
            if left.__len__() != right.__len__():
                return False
            temp_left = []
            temp_right = []
            for i in range(left.__len__()):
                j = left.__len__() - 1 - i
                if left[i] == None or right[j] == None:
                    continue
                if isNodeSame(left[i].left, right[j].right):
                    temp_left.append(left[i].left)
                    temp_right.append(right[j].right)
                else:
                    return False
                if isNodeSame(left[i].right, right[j].left):
                    temp_left.append(left[i].right)
                    temp_right.append(right[j].left)
                else:
                    return False
            left = temp_left
            temp_right.reverse()
            right = temp_right
        return True

n0 = TreeNode(0)
n1 = TreeNode(1)
n0.left = n1
n2 = TreeNode(1)
n0.right = n2
n3 = TreeNode(3)
n2.left = n3
n4 = TreeNode(3)
n1.right = n4
showTree(n0)
so = Solution()
print(so.isSymmetric(n2))