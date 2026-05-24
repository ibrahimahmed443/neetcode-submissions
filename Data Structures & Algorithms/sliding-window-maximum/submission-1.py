class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        max_window = []
        max_n = {}
        m = 0
        for r in range(k -1, len(nums)):
            if l == 0:
                m = max(nums[l:r+1])
                max_n[m] = nums.index(m)
            else:
                if l > max_n[m]:
                    m = max(nums[l:r+1])
                    max_n[m] = nums.index(m)
                elif nums[r] > m:
                    m = nums[r]
                    max_n[m] = r

            max_window.append(m)
            l += 1
        
        return max_window