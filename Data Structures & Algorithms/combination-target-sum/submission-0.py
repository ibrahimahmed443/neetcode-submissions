class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curr, i, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(nums):
                return
            
            curr.append(nums[i])
            dfs(curr, i, total + nums[i])

            curr.pop()
            dfs(curr, i + 1, total)
        
        dfs([], 0, 0)
        return res
