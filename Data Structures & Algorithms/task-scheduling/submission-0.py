class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = 1 + counts.get(task, 0)
        
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()         # pair of [cnts, time_to_add]

        while max_heap or q:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    q.append([cnt, time+n])
            
            if q and q[0][1] == time:
                cnt = q.popleft()[0]
                heapq.heappush(max_heap, cnt)
        
        return time
