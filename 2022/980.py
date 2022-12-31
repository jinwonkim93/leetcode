from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        global ans
        ans = 0
        x_max = len(grid)
        y_max = len(grid[0])
        visited = [[False] * y_max for _ in range(x_max)]

        for row in range(x_max):
            for column in range(y_max):
                if grid[row][column] == -1:
                    visited[row][column] = True
                if grid[row][column] == 1:
                    start_position = (row, column)
                    visited[row][column] = True

        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def check_all_visited(visited):
            for i in range(len(visited)):
                for j in range(len(visited[0])):
                    if visited[i][j] is False:
                        return False
            return True
        
        def dfs(cur_x, cur_y, grid, visited):
            
            if grid[cur_x][cur_y] == 2:
                visited[cur_x][cur_y] = True
                if check_all_visited(visited) is True:
                    global ans
                    ans += 1
                    return
                
            for move in moves:
                next_x = cur_x + move[0]
                next_y = cur_y + move[1]
                if (next_x >= 0 
                    and next_x < x_max
                    and next_y >= 0
                    and next_y < y_max):
                    if visited[next_x][next_y] is False:
                        visited[next_x][next_y] = True
                        dfs(next_x, next_y, grid, visited)
                        visited[next_x][next_y] = False
                    
        dfs(start_position[0], start_position[1], grid, visited)
        return ans