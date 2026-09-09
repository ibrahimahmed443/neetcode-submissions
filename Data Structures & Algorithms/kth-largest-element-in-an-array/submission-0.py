class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        num = None
        for i in range(k):
            num = heapq.heappop(max_heap)
        
        return -num