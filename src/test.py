class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        result = self.val
        curr = self.next
        while curr:
            result += "->" + curr.val
            curr = curr.next
        return result


def reverse_between(head, left, right):
    dummy_node = ListNode("0")
    dummy_node.next = head
    pre = dummy_node
    # 找到指定区间的前一个节点pre
    for _ in range(left - 1):
        pre = pre.next
    curr = pre.next
    # 根据区间长度遍历多次，每次遍历将节点插至pre后面
    for _ in range(right - left):
        t = curr.next
        curr.next = t.next
        t.next = pre.next
        pre.next = t
    return dummy_node.next


n0 = ListNode("a")
n1 = ListNode("b")
n2 = ListNode("c")
n3 = ListNode("d")
n4 = ListNode("e")
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

print(n0)
x = reverse_between(n0, 2, 3)
print(x)