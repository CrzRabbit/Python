'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = None
        second = head
        while second != None:
            if first != None:
                first = first.next
            if n == 0:
                first = head
            n -= 1
            second = second.next
        #self.showList(first)
        print(n)
        if first != None and first.next != None:
            first.next = first.next.next
        elif n == 0:
            head = head.next
        #self.showList(head)
        return head

    def showList(self, l : ListNode):
        temp = l
        str = ''
        while temp != None and temp.next != None:
            str += '{}->'.format(temp.val)
            temp = temp.next
        if temp != None:
            str += '{}'.format(temp.val)
        print(str)

n1 = [1]
l1 = ListNode()
l1.val = n1[0]
l = l1
for i in range(1, len(n1)):
    temp = ListNode()
    temp.val = n1[i]
    l.next = temp
    l = temp
so = Solution()
so.removeNthFromEnd(l1, 2)