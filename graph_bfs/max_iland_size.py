from typing import List

class MaxIlandSize:
    iland_size = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        max_iland = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    self.scan_iland(row,col,grid,visited)
                    max_iland = max(max_iland, self.iland_size)
                    self.iland_size = 0
        return max_iland

    def scan_iland(self, row, col, grid, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 
        if visited[row][col] or grid[row][col] == 0:
            return
        visited[row][col] = True
        self.iland_size += 1
        for direction in [[0,-1],[0,1],[1,0],[-1,0]]:
            self.scan_iland(row+direction[0], col+direction[1], grid, visited)
        return

grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

iland = MaxIlandSize()
print(iland.maxAreaOfIsland(grid)) 

        