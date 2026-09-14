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
        
        if abs(len(self.min_heap) - len(self.max_heap)) > 1:
            if len(self.min_heap) > len(self.max_heap):
                item = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -item)
            else:
                item = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -item)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + (self.max_heap[0] * -1)) / 2
        else:
            if len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return self.max_heap[0] * -1

        