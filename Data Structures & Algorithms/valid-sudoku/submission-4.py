class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for square in range(9):
            row = []
            for i in range(3):
                for j in range(3):
                    r = (square // 3) * 3 + i
                    c = (square % 3) * 3 + j
                    row.append(board[r][c])

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

    def hasDuplicates(self, row):
        seen = set()
        for num in row:
            if num != ".":
                  if num in seen:
                        return True
                  seen.add(num)

        return False