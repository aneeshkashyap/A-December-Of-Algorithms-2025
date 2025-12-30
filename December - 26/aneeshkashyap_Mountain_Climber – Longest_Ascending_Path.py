import sys
sys.setrecursionlimit(10000)

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

dp = [[0]*N for _ in range(M)]  # memoization table

def dfs(r, c):
    if dp[r][c] != 0:
        return dp[r][c]
    
    length = 1  # at least the current cell
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] > grid[r][c]:
            length = max(length, 1 + dfs(nr, nc))
    dp[r][c] = length
    return length

max_path = 0
for i in range(M):
    for j in range(N):
        max_path = max(max_path, dfs(i,j))

print(max_path)
3 