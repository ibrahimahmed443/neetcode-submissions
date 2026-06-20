class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        top = 0
        bottom = rows - 1
        found = False
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                found = True
                break
            
        if not found:
            return False
        
        left = 0
        right = cols - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            
            if matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
