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
showTree(so.sortedListToBST(got_list([-10, -3, 0, 5, 9])), 3)