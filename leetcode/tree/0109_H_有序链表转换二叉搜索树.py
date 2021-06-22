'''
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
'''
from leetcode.tools.tree import *
from leetcode.tools.list import *
class Solution:
    def sortedListToBST(self, head) -> TreeNode:
        if not head:
            return None
        left = head
        right = head
        temp = None
        while right:
            right = right.next
            if not right:
                break
            else:
                right = right.next
                if right:
                    if not temp:
                        temp = left
                    else:
                        temp = temp.next
                    left = left.next
                else:
                    break
        root = TreeNode(left.val)
        if temp:
            temp.next = None
            root.left = self.sortedListToBST(head)
        if left.next:
            root.right = self.sortedListToBST(left.next)
        return root

so = Solution()
showTree(so.sortedListToBST(getList([-10, -3, 0, 5, 9])), 3)