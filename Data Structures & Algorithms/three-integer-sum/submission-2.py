class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range((len(nums))):
            if nums[i] > 0:
                break   # In a sorted array if 1st element > 0, there is no solution

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left+= 1
                    while nums[left] == nums[left-1] and left < right:
                        left+= 1
                    
        return result
