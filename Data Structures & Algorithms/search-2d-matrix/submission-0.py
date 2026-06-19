class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [num for row in matrix for num in row]
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                return True
            
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return False