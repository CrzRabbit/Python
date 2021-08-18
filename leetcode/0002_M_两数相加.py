'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    依次遍历，逐位相加，保存进位
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #l_1re = self.reverse_list(l1)
        #l2_re = self.reverse_list(l2)
        l3 = None
        temp1 = l1
        temp2 = l2
        temp3 = l3
        rest = 0
        while temp1 != None or temp2 != None:
            t1 = 0
            t2 = 0
            if temp1:
                t1 = temp1.val
                temp1 = temp1.next
            if temp2:
                t2 = temp2.val
                temp2 = temp2.next
            node = ListNode()
            node.val = (rest + t1 + t2) % 10
            rest = (int)((rest + t1 + t2) / 10)
            if l3 is None:
                l3 = node
                temp3 = l3
            else:
                temp3.next = node
                temp3 = temp3.next
        if rest == 1:
            node = ListNode()
            node.val = 1
            temp3.next = node
        self.showList(l3)
        return l3

    def reverse_list(self, l : ListNode):
        temp1 = l
        temp2 = None
        while temp1.next != None:
            temp3 = temp1
            temp1 = temp1.next
            temp3.next = temp2
            temp2 = temp3
        temp1.next = temp2
        self.showList(temp1)
        return temp1

    def showList(self, l : ListNode):
        temp = l
        str = ''
        while temp.next != None:
            str += '{}->'.format(temp.val)
            temp = temp.next
        str += '{}'.format(temp.val)
        print(str)

n1 = [2, 4, 9]
l1 = ListNode()
l1.val = n1[0]
l = l1
for i in range(1, len(n1)):
    temp = ListNode()
    temp.val = n1[i]
    l.next = temp
    l = temp

n2 = [5, 6, 4, 9]
l2 = ListNode()
l2.val = n2[0]
l = l2
for i in range(1, len(n2)):
    temp = ListNode()
    temp.val = n2[i]
    l.next = temp
    l = temp
so = Solution()
so.addTwoNumbers(l1, l2)