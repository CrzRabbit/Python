'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''
from leetcode.tools.list import *
from leetcode.tools.time import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ret = ListNode()
        ret.next = head
        left = ret
        right = None
        temp1 = ret
        temp2 = None
        while True:
            showList(ret.next)
            if temp1 != None:
                temp1 = temp1.next
            else:
                break
            if temp1 != None:
                temp2 = temp1.next
            else:
                break
            if temp1 != None and temp2 != None:
                right = temp2.next
                temp2.next = temp1
                temp1.next = right
                left.next = temp2
                left = temp1
            else:
                break
        return ret.next
so = Solution()
showList(so.swapPairs(getList([1, 2, 3])))