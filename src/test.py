class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_elements(head: ListNode, val: int) -> ListNode:
    sentinel = ListNode(0)
    sentinel.next = head

    prev, curr = sentinel, head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return sentinel.next