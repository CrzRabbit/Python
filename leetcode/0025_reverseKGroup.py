from leetcode.tools.list import *
from leetcode.tools.time import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ret = ListNode()
        ret.next = head
        part = []
        left = ret
        right = None
        temp = head
        while temp != None and len(part) < k:
            part.append(temp)
            temp = temp.next
        right = temp
        if len(part) == k:
            for i in range(1, len(part)):
                part[i].next = part[i - 1]
            left.next = part[len(part) - 1]
            part[0].next = right
            left = part[0]
            temp = right
        while len(part) == k:
            part.clear()
            while temp != None and len(part) < k:
                part.append(temp)
                temp = temp.next
            right = temp
            if len(part) == k:
                for i in range(1, len(part)):
                    part[i].next = part[i - 1]
                left.next = part[len(part) - 1]
                part[0].next = right
                left = part[0]
                temp = right
        return ret.next

so = Solution()
showList(so.reverseKGroup(getList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 8))