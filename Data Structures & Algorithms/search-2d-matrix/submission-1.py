class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m * n - 1

        while start <= end:
            mid = start + ((end - start) // 2)
            num = self.getNumberAtIndex(matrix, mid)
            if num == target:
                return True
            
            if num < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return False

    def getNumberAtIndex(self, matrix, index):
        n = len(matrix[0])
        row, col = index // n, index % n
        return matrix[row][col]
