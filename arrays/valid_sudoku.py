from typing import List

class Solution:

    def is_invalid(row, col, board):
        target = board[row][col]

        d_row = row
        d_col = col

        def verify_row():
            for i in range(d_row+1, 9):
                if board[i][d_col] == target:
                    print(f"row: {i}, col: {d_col} == {target} at verify_row")
                    return False
            for i in range(d_row-1, -1, -1):
                if board[i][d_col] == target:
                    print(f"row: {i}, col: {d_col} == {target} at verify_row")
                    return False
            return True

        def verify_col():
            for i in range(d_col+1, 9):
                if board[d_row][i] == target:
                    print(f"row: {d_row}, col: {i} == {target} at verify_col")
                    return False
            for i in range(d_col-1, -1, -1):
                if board[d_row][i] == target:
                    print(f"row: {d_row}, col: {i} == {target} at verify_col")
                    return False
            return True

        def verify_grid():
            root_idx = [0,0,0,3,3,3,6,6,6]
            r_row = root_idx[d_row]
            c_col = root_idx[d_col]
            cnt = 0
            for row in range(r_row, r_row + 3):
                for col in range(c_col, c_col + 3):
                    if board[row][col] == target:
                        # print(f"row: {row}, col: {col} == {target} at verify_grid grid search actual {r_row} {c_col} grid search full {r_row + 3} {c_col + 3}")
                        cnt += 1
            # print(f"total count {cnt} verfication check {cnt == 1} at verify_grid for target {target} grid {r_row} {c_col}")
            return cnt == 1

        if verify_row():
            if verify_col():
                if verify_grid():
                    return True

        return False

    def isValidSudoku(board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] != '.':
                    if not self.is_invalid(row, col, board):
                        return False
        return True
    
sudoku = Solution()

board = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

diff_board = [["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","8",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]

print(sudoku.isValidSudoku(board))
