class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LruCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.size = 0
        self.dumb_head = Node(None, None)
        self.dumb_tail = Node(None, None)
        self.dumb_head.next = self.dumb_tail
        self.dumb_tail.pre = self.dumb_head

    @staticmethod
    def delete_node(node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def add2head(self, node):
        node.next = self.dumb_head.next
        self.dumb_head.next.pre = node
        self.dumb_head.next = node
        node.pre = self.dumb_head

    def set(self, key, value):
        if key in self.dic:
            node = self.dic[key]
            node.value = value
            self.delete_node(node)
            self.add2head(node)
        else:
            if self.size == self.capacity:
                self.dic.pop(self.dumb_tail.pre.key)
                self.delete_node(self.dumb_tail.pre)
            else:
                self.size += 1
            node = Node(key, value);
            self.add2head(node)
            self.dic[key] = node

    def get(self, key):
        if key not in self.dic:
            return None
        node = self.dic.get(key)
        self.delete_node(node)
        self.add2head(node)
        return node.value


cache = LruCache(2)
cache.set(1, 10)
cache.set(2, 20)
print(cache.get(1))  # 10
cache.set(3, 30)
print(cache.get(2))  # None
cache.set(4, 40)
print(cache.get(1))  # None
print(cache.get(3))  # 30
print(cache.get(4))  # 40
