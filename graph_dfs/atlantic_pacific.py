def atlantic_pacific_reach(grid):
    ROWS, COLS = len(grid), len(grid[0])
    pac, atl = set(), set()

    def dfs(row, col, visit, prevState):
        if (
            (row, col) in visit or
            min(row, col) < 0 or
            row == ROWS or
            col == COLS or
            grid[row][col] < prevState
        ):
            return 
        visit.add((row, col))
        dfs(row + 1, col, visit, grid[row][col])
        dfs(row - 1, col, visit, grid[row][col])
        dfs(row, col + 1, visit, grid[row][col])
        dfs(row, col - 1, visit, grid[row][col])
    
    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS-1, c, atl, heights[ROWS-1][c])
    
    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS-1, atl, heights[r][COLS-1])

    result = []

    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r,c) in atl:
                result.append((r,c))
    
    return result

heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]

print(atlantic_pacific_reach(heights))
