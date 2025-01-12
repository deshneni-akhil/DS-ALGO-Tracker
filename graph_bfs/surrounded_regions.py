from collections import deque
from typing import List

class SurroundedRegions:

    # Time complexity: O(N*M) ^ 2 & Space complexity: O(N*M)
    def approach_long(self, board):
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row, col) not in visit:
                    region = deque()
                    self.find_region(row, col, board, visit, region)
                    self.surround_region(region, board)
        return
    
    def approach_short(self, board):
        ROWS, COLS = len(board), len(board[0])

        def dfs_helper(row, col):
            if min(row, col) < 0 or row == ROWS or col == COLS or board[row][col] != 'O':
                return 
            board[row][col] = 'T'
            dfs_helper(row+1, col)
            dfs_helper(row-1, col)
            dfs_helper(row, col+1)
            dfs_helper(row, col-1)
        
        for row in range(ROWS):
            for col in range(COLS):
                if row in [0, ROWS-1] or col in [0, COLS-1]:
                    dfs_helper(row, col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'
        return

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # self.approach_long(board)
        self.approach_short(board)
        return

    def surround_region(self, region, board):
        buffer = region.copy()
        can_surrounded = True
        while region:
            row, col = region.popleft()
            if not self.can_surrounded(row, col, board):
                can_surrounded = False
                break
        
        if can_surrounded:
            while buffer:
                row, col = buffer.popleft()
                board[row][col] = 'X'

    def can_surrounded(self, row, col, board):
        ROWS, COLS = len(board), len(board[0])
        up = down = left = right = False
        
        ur = row
        # up direction 
        for ur in range(ur-1, -1, -1):
            if board[ur][col] == 'X':
                up = True
                break 
        
        dr = row
        # down direction
        for dr in range(dr+1, ROWS):
            if board[dr][col] == 'X':
                down = True
                break
        
        lc = col
        # left direction
        for lc in range(lc-1, -1, -1):
            if board[row][lc] == 'X':
                left = True
                break
        
        rc = col
        # right direction
        for rc in range(rc+1, COLS):
            if board[row][rc] == 'X':
                right = True
                break
        
        return left & right & up & down
    
    def find_region(self, row, col, board, visit, nodes):
        if (
            min(row, col) < 0 or
            (row, col) in visit or
            row >= len(board) or
            col >= len(board[0]) or
            board[row][col] == 'X'
        ):
            return
        nodes.append((row,col))
        visit.add((row,col))
        self.find_region(row + 1, col, board, visit, nodes)
        self.find_region(row - 1 , col, board, visit, nodes)
        self.find_region(row , col + 1, board, visit, nodes)
        self.find_region(row , col - 1, board, visit, nodes)
        return
        
# Test
board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
sr = SurroundedRegions()
sr.solve(board)
print(board)