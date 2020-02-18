class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_intersection_node(head_a: ListNode, head_b: ListNode) -> ListNode:
    ha, hb = head_a, head_b
    while ha != hb:
        ha = ha.next if ha else head_b
        hb = hb.next if hb else head_a
    return ha