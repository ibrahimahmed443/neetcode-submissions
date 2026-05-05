class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for n in nums:
            if counts.get(n):
                return True
            
            counts[n] = 1

        return False