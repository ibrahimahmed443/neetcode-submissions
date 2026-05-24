class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        maxWindow = []
        for r in range(k -1, len(nums)):
            maxWindow.append(max(nums[l:r+1]))
            l += 1
        
        return maxWindow