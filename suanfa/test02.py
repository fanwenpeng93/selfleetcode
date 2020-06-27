"""
主要是链表算法
"""
"""
判断链表是否有环
"""
def t01(head):
    fast=head.next.next
    slow=head
    if fast!=None and slow!=None:
        fast=head.next.next
        slow=head.next
        if fast==slow:
            return True
    return False

"""
反转链表
"""

def t02(head):
    if head==None:
        return head
    nextwill=None
    if head.next!=None:
        temp=head.next
        head.next=nextwill
        head=temp
        nextwill=head
        return nextwill
"""
获取链表的倒数第n个节点
"""
def t03(head,n):
    before=head
    after=head
    for i in range(n-1):
        after=after.next
    while before.next!=None and after.next!=None:
        before=before.next
        after=after.next
        if after.next==None:
            return before
"""
合并两个有序链表
"""
def t04(h01,h02):
    if h01==None and h02!=None:
        return h02
    elif h01!=None and h02==None:
        return h01
    elif h01!=None and h02!=None:
        return None
    else:
        if h01.data>h02.data:
            h02.next=t04(h02.next,h01)
            return h02
        else:
            h01.next=t04(h01.next,h02)
            return h01


"""
从尾到头打印链表
"""
def t05(head):
    if head==None:
        return None
    r=[]
    while head.next!=None:
        r.append(head.data)
        head=head.next
    return r[::-1]










