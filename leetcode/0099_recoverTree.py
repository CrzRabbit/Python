from leetcode.tools.tree import *
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorderTraversal(root: TreeNode):
            ret = []
            if root == None:
                return ret
            if root.left != None:
                ret += inorderTraversal(root.left)
            ret.append(root)
            if root.right != None:
                ret += inorderTraversal(root.right)
            return ret
        nodes = inorderTraversal(root)
        num = nodes.__len__() - 1
        exchange = True
        while num != 0 and exchange:
            exchange = False
            for i in range(0, num):
                if nodes[i].val > nodes[i + 1].val:
                    nodes[i].val = nodes[i].val ^ nodes[i + 1].val
                    nodes[i + 1].val = nodes[i].val ^ nodes[i + 1].val
                    nodes[i].val = nodes[i].val ^ nodes[i + 1].val
                    exchange = True
            num -= 1

n0 = TreeNode(0)
n1 = TreeNode(1)
n0.left = n1
n2 = TreeNode(2)
n0.right = n2
n3 = TreeNode(3)
n2.left = n3

so = Solution()
showTree(n0)
morrisTraverse(n0)
so.recoverTree(n0)
showTree(n0)