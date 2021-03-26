class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getList(nodes):
    if len(nodes) == 0:
        return None
    head = ListNode()
    head.val = nodes[0]
    l = head
    for i in range(1, len(nodes)):
        temp = ListNode()
        temp.val = nodes[i]
        l.next = temp
        l = temp
    return head

def showList(l : ListNode):
    temp = l
    str = ''
    while temp != None and temp.next != None:
        str += '{}->'.format(temp.val)
        temp = temp.next
    if temp != None:
        str += '{}'.format(temp.val)
    print(str)