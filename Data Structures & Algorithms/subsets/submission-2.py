class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def sub(p, i):
            if i == len(nums):
                out.append(p[:])
                return
            
            p.append(nums[i])
            sub(p, i + 1)
            p.pop()
            sub(p, i + 1)

        sub([], 0)
        return out