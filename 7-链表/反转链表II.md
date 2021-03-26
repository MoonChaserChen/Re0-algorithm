# 反转链表II
将给出的链表中的节点每 k 个一组翻转，返回翻转后的链表
如果链表中的节点数不是 k 的倍数，将最后剩下的节点保持原样
你不能更改节点中的值，只能更改节点本身。
要求空间复杂度 O(1)

```
例如：
给定的链表是1 → 2 → 3 → 4 → 5
对于 k = 2, 你应该返回 2 → 1 → 4 → 3 → 5
对于 k = 3, 你应该返回 3 → 2 → 1 → 4 → 5
```

来源：[NowCoder](https://www.nowcoder.com/practice/b49c3dc907814e9bbfa8437c251b028e?tpId=188)

## 每次翻转K个
每次翻转K个，然后再拼起来
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def reverse_k_group(head, k):
    # 以th为头，翻转k个元素。若不足k个元素，不翻转
    # 返回值：下一组的头，当前组翻转后的头，当前组翻转后的尾
    def reverse(th):
        if not th:
            return None, None, None
        tt = th
        for i in range(k - 1):
            if tt.next:
                tt = tt.next
            else:
                return None, th, tt
        p, c = None, th
        while c and p != tt:
            t = c.next
            c.next = p
            p = c
            c = t
        return c, tt, th
    curr, tt1, th1 = reverse(head)
    # 通过每组的尾tail拼接下一组的头
    tail = th1
    re = tt1
    while curr:
        curr, tt1, th1 = reverse(curr)
        tail.next = tt1
        tail = th1
    return re
```

## 递归思想
`reverse_k_group` 方法要定位到下个迭代开始节点，分组时需要多走一次，即`for i in range(k):`，因此在翻转时也需要忽略最后一个节点
```python
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
```

## 栈
但是空间复杂度为O(K)，不符合要求，这里仅仅作为参照：
