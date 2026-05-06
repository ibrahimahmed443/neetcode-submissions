class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            curr = nums[i]
            x = target - curr

            if map.get(x) is not None:
                return [map.get(x), i]

            map[curr] = i


