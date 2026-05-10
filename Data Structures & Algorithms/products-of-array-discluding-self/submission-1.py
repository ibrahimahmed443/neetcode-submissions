class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0

        # find prod of non-zero numbers
        prod = 1
        for num in nums:
            if num:
                prod = prod * num
            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if zero_count:
                res[i] = 0 if num else prod
            else:
                res[i] = prod // num
        
        return res

