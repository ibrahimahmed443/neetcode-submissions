class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            self.min_heap.append(num)
            heapq.heapify(self.min_heap)
        else:
            self.max_heap.append(-num)
            heapq.heapify(self.max_heap)

        if len(self.min_heap) > len(self.max_heap) + 1:
            item = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -item)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            item = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -item)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return self.max_heap[0] * -1
        else:
            return (self.min_heap[0] + (self.max_heap[0] * -1)) / 2

        