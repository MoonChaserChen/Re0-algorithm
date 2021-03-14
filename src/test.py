class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

#
#
# @param head ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def reverse_k_group(self, head, k):
        if not head:
            return head
        h = t = head
        for i in range(k):
            if not t:
                return head
            t = t.next
        new_head = reverse(h, t)
        h.next = self.reverse_k_group(t, k)
        return new_head


# [h, t) 翻转
def reverse(h, t):
    p, c = None, h
    while c != t:
        temp = c.next
        c.next = p
        p = c
        c = temp
    return p


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
# n5.next = n6


r = Solution().reverse_k_group(n1, 3)
print(r)