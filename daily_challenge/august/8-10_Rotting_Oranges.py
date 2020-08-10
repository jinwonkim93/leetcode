from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    q.append((x,y,0))
        ans = 0

        while len(q) != 0:
            x,y,count = q.popleft()
            ans = max(ans,count)
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx = x+dx
                ny = y+dy
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]): continue

                if grid[nx][ny] == 1:
                    q.append((nx,ny,count+1))
                    grid[nx][ny] = 2

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    return -1
        return ans