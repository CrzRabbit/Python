class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        up = l1
        down = l2
        head = None
        ret = None
        temp = None
        while up != None or down != None:
            if up != None and down != None:
                if up.val < down.val:
                    temp = up
                    up = up.next
                else:
                    temp = down
                    down = down.next
            elif up == None:
                if head == None:
                    return down
                ret.next = down
                break
            elif down == None:
                if head == None:
                    return up
                ret.next = up
                break
            if head == None:
                head = temp
                ret = temp
            else:
                ret.next = temp
                ret = temp
            return head