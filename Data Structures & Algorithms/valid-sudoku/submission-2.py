class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                row = self.getDiagonal(board, m, n)
                if self.hasDuplicates(row):
                    return False

        for row in board:
            if self.hasDuplicates(row):
                return False
        
        for col in range(0, 9):
            row = [row[col] for row in board]
            if self.hasDuplicates(row):
                return False
                
        return True

    def getDiagonal(self, board, m, n):
        row = []
        for i in range(m, m+3):
            for j in range(n, n+3):
                row.append(board[i][j])
        
        return row

    def hasDuplicates(self, row):
        seen = set()
        for num in row:
            if num != ".":
                  if num in seen:
                        return True
                  seen.add(num)

        return False