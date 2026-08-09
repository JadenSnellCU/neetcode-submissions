from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row = Counter(board[i])
            col = Counter(board[r][i] for r in range(9))

            for key, value in row.items():
                if key != "." and value > 1:
                    return False

            for key, value in col.items():
                if key != "." and value > 1:
                    return False

        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                cube = Counter(
                    board[r][c]
                    for r in range(row_start, row_start + 3)
                    for c in range(col_start, col_start + 3)
                )

                for key, value in cube.items():
                    if key != "." and value > 1:
                        return False

        return True