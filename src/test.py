# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = str(self.val)
        curr = self.next
        while curr:
            res += "->" + str(curr.val)
            curr = curr.next
        return res


def delete_duplicates(head: ListNode, pv=None) -> ListNode:
    if not head:
        return head
    if pv is not None and head.val == pv or head.next and head.val == head.next.val:
        return delete_duplicates(head.next, head.val)
    else:
        head.next = delete_duplicates(head.next, head.val)
        return head


l0 = ListNode(1)
l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(3)
l5 = ListNode(3)
l6 = ListNode(5)
l7 = ListNode(7)
l8 = ListNode(7)

l0.next = l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8

r = delete_duplicates(l0)
print(r)