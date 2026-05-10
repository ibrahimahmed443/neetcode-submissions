class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]

        res = [1] * len(nums)

        prefix, suffix = 1, 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * suffix
            suffix = suffix * nums[i]

        return res
