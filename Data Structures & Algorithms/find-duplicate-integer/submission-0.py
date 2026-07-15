class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        for k, v in counts.items():
            if v != 1:
                return k
