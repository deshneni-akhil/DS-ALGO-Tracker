from collections import deque

neighbours = [[1,0],[-1,0],[0,-1],[0,1]]

def approach_long(grid):
    rows, cols = len(grid), len(grid[0])
    goals = deque()
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                goals.append((row,col))
    
    while goals:
        row, col = goals.popleft()
        visited[row][col] = True
        for neighbour in neighbours:
            neir = row + neighbour[0]
            neic = col + neighbour[1]
            if isValid(neir, neic, grid) and not visited[neir][neic]:
                value = fetchValue(grid, neir, neic, neighbours)
                grid[neir][neic] = value 
                goals.append((neir, neic))
    return  


def approach_short(grid):
    ROWS, COLS = len(grid), len(grid[0])
    q = deque()
    visit = set()

    def addCell(row, col):
        if (
            min(row,col) < 0 or
            row == ROWS or
            col == COLS or
            (row, col) in visit or
            grid[row][col] == -1
        ):
            return 
        visit.add((row,col))
        q.append((row, col))

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 0:
                q.append((row, col))
                visit.add((row, col))
    
    distance = 0
    while q:
        for _ in range(len(q)):
            row, col = q.popleft()
            grid[row][col] = distance
            addCell(row+1, col)
            addCell(row-1, col)
            addCell(row, col+1)
            addCell(row, col-1)
        distance += 1
    return 


def ilands_treasure(grid):
    # approach_long(grid)
    approach_short(grid)
    return 

def fetchValue(grid, row, col, neighbours):
    min_value = grid[row][col]
    for neighbour in neighbours:
        neir = row + neighbour[0]
        neic = col + neighbour[1]
        if isValid(neir, neic, grid):
            min_value = min(min_value, grid[neir][neic])
    return min_value + 1

def isValid(row, col, grid):
    rows, cols = len(grid), len(grid[0])

    if (row < 0 or row >= rows) or (col < 0 or col >= cols) or grid[row][col] == -1:
        return False

    return True

grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

ilands_treasure(grid)

print(grid)