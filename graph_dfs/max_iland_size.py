from typing import List

class MaxIlandSize:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        max_iland = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    iland_size = self.scan_iland(row,col,grid,visited)
                    max_iland = max(max_iland, iland_size)
        return max_iland

    def scan_iland(self, row, col, grid, visited) -> int:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0
        if visited[row][col] or grid[row][col] == 0:
            return 0
        visited[row][col] = True
        area = 1
        for direction in [[0,-1],[0,1],[1,0],[-1,0]]:
            area += self.scan_iland(row+direction[0], col+direction[1], grid, visited)
        return area

grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

iland = MaxIlandSize()
print(iland.maxAreaOfIsland(grid)) 

        