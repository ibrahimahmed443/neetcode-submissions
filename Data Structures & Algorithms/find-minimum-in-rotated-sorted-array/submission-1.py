class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums) - 1
        left = 0
        right = n

        while left <= right:
            mid = (left + right) // 2
            print(nums[left], nums[mid], nums[right])
            if nums[left] < nums[mid]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            else:
                break

        if nums[left] == nums[right] == nums[mid]:
            return nums[0]

        return nums[right]
