# 删除排序链表中的重复元素
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。

返回同样按升序排列的结果链表。

来源：[LeetCode](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii)

```
示例 1:
    输入: 1->2->3->3->4->4->5
    输出: 1->2->5
    
示例 2:
    输入: 1->1->1->2->3
    输出: 2->3
```

## 双指针
双指针思想，快指针fc用于遍历链表，慢指针sc用于提取需要的结果重构链表
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head: ListNode) -> ListNode:
    dummy_node = ListNode(0, head)
    sc, fc = dummy_node, head
    # fc上个节点值
    temp = None
    while fc:
        if (temp is None or temp != fc.val) and (fc.next or fc.next.val != fc.val):
            sc.next = fc
            sc = sc.next
        else:
            sc.next = None
        temp = fc.val
        fc = fc.next
    return dummy_node.next
```

## 单指针双循环
先找到重复值，再不断跳过
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head: ListNode) -> ListNode:
    if not head:
        return head
    dummy = ListNode(0, head)
    cur = dummy
    while cur.next and cur.next.next:
        if cur.next.val == cur.next.next.val:
            x = cur.next.val
            while cur.next and cur.next.val == x:
                cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next
```