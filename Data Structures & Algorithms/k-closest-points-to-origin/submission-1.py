class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0, 0]
        min_heap = []
        for point in points:
            dist = (point[0] - origin[0]) ** 2 + (point[1] - origin[1]) ** 2
            min_heap.append((dist, point))
        
        heapq.heapify(min_heap)

        output = []
        for i in range(k):
            output.append(heapq.heappop(min_heap)[1])

        return output