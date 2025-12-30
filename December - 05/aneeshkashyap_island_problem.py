grid = []
n = int(input())          # number of rows
for _ in range(n):
    grid.append(list(map(int, input().split())))

rows = len(grid)
cols = len(grid[0])
count = 0

def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if grid[r][c] == 0:
        return

    grid[r][c] = 0       # mark as visited

    dfs(r+1, c)
    dfs(r-1, c)
    dfs(r, c+1)
    dfs(r, c-1)

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:
            count += 1
            dfs(i, j)

print(count)
