'''
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
'''
from leetcode.tools.list import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        up = True
        down = True
        uptr = headA
        dptr = headB
        while uptr and dptr:
            if uptr == dptr:
                return uptr
            else:
                if up and not uptr.next:
                    uptr = headB
                    up = False
                else:
                    uptr = uptr.next
                if down and not dptr.next:
                    dptr = headA
                    down = False
                else:
                    dptr = dptr.next
        return None