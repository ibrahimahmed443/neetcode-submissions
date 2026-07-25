class Node:         
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    # Doubly Linked List layout: head <-> MRU .... <-> LRU <-> tail   
    # head and tail are dummy nodes

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}         # key, <Node>
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def _add_to_front(self, node):
        first = self.head.next      # original next node
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node

    def _move_to_front(self, node):
        self._remove(node)
        self._add_to_front(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            # move this node to front
            node = self.cache[key]
            self._move_to_front(node)   # move it to most recently used
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)   # move it to most recently used
        else:
            # create a new <key, Node> pair
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)

            if len(self.cache) > self.capacity:
                # Evict the least recently used node, which is close to tail
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            
        