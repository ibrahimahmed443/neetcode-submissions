class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        # find prod of non-zero numbers
        prod = 1
        for num in nums:
            if num != 0:
                prod = prod * num
        
        res = []
        for num in nums:
            if zero_count == 0:
                res.append(prod // num)
            else:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
        
        return res

