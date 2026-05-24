class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        l = 0
        for r in range(len(nums)):
            if q and l > q[0]:    # is top element out of the window?
                q.popleft()

            # q is in decreasing order. So maintain max value at left
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            if r + 1 >= k:
                result.append(nums[q[0]])
                l += 1
        
        return result
