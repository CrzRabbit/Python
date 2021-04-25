'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：

你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''
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