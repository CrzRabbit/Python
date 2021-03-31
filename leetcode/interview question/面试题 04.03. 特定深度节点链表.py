from leetcode.tools.tree import *
from leetcode.tools.list import *
class Solution:
    def listOfDepth(self, tree: TreeNode):
        ret = []
        nodes = []
        if not tree:
            return ret
        nodes.append(tree)
        while nodes.__len__():
            temp_nodes = []
            temp_list = None
            for node in nodes:
                if node.left:
                    temp_nodes.append(node.left)
                if node.right:
                    temp_nodes.append(node.right)
                listNode = ListNode(node.val)
                if temp_list:
                    temp_list.next = listNode
                    temp_list = listNode
                if not temp_list:
                    temp_list = listNode
                    ret.append(listNode)
            nodes = temp_nodes
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
showTree(n0)
so = Solution()
for l in so.listOfDepth(n0):
    showList(l)

