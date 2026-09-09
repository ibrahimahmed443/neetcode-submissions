import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k):
            pivot = random.choice(nums)
            low = [num for num in nums if num < pivot]
            eq = [num for num in nums if num == pivot]
            high = [num for num in nums if num > pivot]

            if k <= len(high):
                return quickSelect(high, k)
            elif k <= len(eq) + len(high):
                return pivot
            else:
                return quickSelect(low, k - len(high) - len(eq))
        
        return quickSelect(nums, k)
