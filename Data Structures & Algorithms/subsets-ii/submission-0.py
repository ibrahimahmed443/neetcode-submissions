class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(subset, i):
            if i == len(nums):
                res.append(subset[:])
                return
            
            # subsets that include nums[i]
            subset.append(nums[i])
            backtrack(subset, i + 1)
            subset.pop()

            # subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(subset, i + 1)
        
        backtrack([], 0)
        return res

    