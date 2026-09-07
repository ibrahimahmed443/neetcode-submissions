class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python has only min-heap, no max-heap
        # To simulate, store neg numbers, and while retrieving turn them to +ve

        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            top1 = -max_heap[0]
            top2 = max(abs(max_heap[1]), abs(max_heap[2])) if len(max_heap) > 2 else abs(max_heap[1])

            heapq.heappop(max_heap)
            heapq.heappop(max_heap)
            if top1 != top2:
                new = top1 - top2
                heapq.heappush(max_heap, -new)
        
        return -max_heap[0] if len(max_heap) > 0 else 0

