class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        # min heap with at most k values
        self._heapify()
        while len(self.heap) > k:
            self.pop()

    def _left_child(self, i):
        return 2 * i + 1
    
    def _right_child(self, i):
        return 2 * i + 2
    
    def _parent(self, i):
        return (i - 1) // 2
    
    def _sift_up(self, i):
        # At i = 0, _parent(0) = (0-1)//2 = -1, so don't include i = 0
        while i > 0 and self.heap[i] < self.heap[self._parent(i)]:
            self.heap[self._parent(i)], self.heap[i] = self.heap[i], self.heap[self._parent(i)]
            i = self._parent(i)

    def _sift_down(self, i):
        n = len(self.heap)

        while True:
            smallest = i
            left = self._left_child(i)
            right = self._right_child(i)

            if left < n and self.heap[smallest] > self.heap[left]:
                smallest = left
            if right < n and self.heap[smallest] > self.heap[right]:
                smallest = right

            if smallest == i:
                break
            
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
    
    def _heapify(self):
        n = len(self.heap)

        # Start at the last non-leaf node and sift down to the root node
        for i in range(n // 2 -1, -1, -1):
            self._sift_down(i)

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        top = self.heap[0]

        # Swap the top with the last element, remove the last, and sift down
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self._sift_down(0)
        return top

    def add(self, val: int) -> int:
        self.push(val)
        
        if len(self.heap) > self.k:
            self.pop()
        
        return self.heap[0]
