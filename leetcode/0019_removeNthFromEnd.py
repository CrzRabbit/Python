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
            if n >= 0:
                n -= 1
            if n == -1:
                first = head
            second = second.next
        self.show_list(first)
        print(n)
        if first != None and first.next != None:
            first.next = first.next.next
        elif n == -1:
            head = head.next
        self.show_list(head)
        return head

    def show_list(self, l : ListNode):
        temp = l
        str = ''
        while temp != None and temp.next != None:
            str += '{}->'.format(temp.val)
            temp = temp.next
        if temp != None:
            str += '{}'.format(temp.val)
        print(str)

n1 = [1, 2, 3, 4]
l1 = ListNode()
l1.val = n1[0]
l = l1
for i in range(1, len(n1)):
    temp = ListNode()
    temp.val = n1[i]
    l.next = temp
    l = temp
so = Solution()
so.removeNthFromEnd(l1, 0)