class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse_list(head: ListNode) -> ListNode:
    if not head or not head.next: return head
    p = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return p