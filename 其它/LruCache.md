# LruCache
Design a data structure for LRU Cache. It should support the following operations: get and set.

| Method | Description |
| ---- | ---- |
| get(key) | Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1. |
| set(key, value) | Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item. |

## Java-HashMap实现
```java
public class LruCache<K, V> {
    private int capacity;
    private int size;
    private Map<K, Node<K, V>> innerMap = new HashMap<>();
    private Node<K, V> dumbHead;
    private Node<K, V> dumbTail;

    public LruCache(int capacity) {
        this.capacity = capacity;
        this.dumbHead = new Node<>(null, null);
        this.dumbTail = new Node<>(null, null);
        dumbHead.next = dumbTail;
        dumbTail.pre = dumbHead;
    }

    public void set(K key, V value) {
        // 包含值：更新值、移节点到头(delete+add)
        if (innerMap.containsKey(key)) {
            Node<K, V> node = innerMap.get(key);
            node.value = value;
            deleteNode(node);
            add2Head(node);
        } else {
            Node<K, V> node = new Node<>(key, value);
            // 不包含值&容量满：删除尾节点、增加头节点
            if (size == capacity) {
                innerMap.remove(dumbTail.pre.key);
                deleteNode(dumbTail.pre);
            } else {
                // 不包含值&容量满：删除尾节点、增加头节点
                size++;
            }
            innerMap.put(key, node);
            add2Head(node);
        }
    }

    public V get(K key) {
        Node<K, V> node = innerMap.get(key);
        if (node == null) {
            return null;
        }
        // 移节点到头(delete+add)
        deleteNode(node);
        add2Head(node);
        return node.value;
    }
    
    private void add2Head(Node<K, V> node) {
        node.next = dumbHead.next;
        dumbHead.next.pre = node;
        dumbHead.next = node;
        node.pre = dumbHead;
    }

    private void deleteNode(Node<K, V> node) {
        node.pre.next = node.next;
        node.next.pre = node.pre;
    }

    public static class Node<K, V> {
        private K key;
        private V value;
        private Node<K, V> pre;
        private Node<K, V> next;

        public Node(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }
}
```

## Java-LinkedHashMap实现
```java
public class LruCache<K, V> extends LinkedHashMap<K, V> {
    private final int capacity;

    public LruCache(int capacity) {
        super(capacity, 0.75f, true);
        this.capacity = capacity;
    }

    @Override
    protected boolean removeEldestEntry(Map.Entry<K, V> eldest) {
        return size() > capacity;
    }
}
```

```java
public class LruCacheTest {
    @Test
    public void testCache() {
        LruCache<Integer, Integer> cache = new LruCache<>(2);
        cache.set(1, 10);
        cache.set(2, 20);
        assertEquals(10, cache.get(1).intValue());
        cache.set(3, 30);
        assertNull(cache.get(2));
        cache.set(4, 40);
        assertNull(cache.get(1));
        assertEquals(30, cache.get(3).intValue());
        assertEquals(40, cache.get(4).intValue());
    }
}
```

## Python实现
```python
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
```
