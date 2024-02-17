import sys
sys.setrecursionlimit(10**6)
def dfs(x, y):
    global size
    graph[x][y] = 1
    size += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < M and 0 <= ny < N and graph[nx][ny] != 1:
            dfs(nx,ny)

input = sys.stdin.readline

M, N, K = map(int, input().split())

graph = [[0]*N for _ in range(M)]

for i in range(K):
    sx, sy, ex, ey = list(map(int, input().split()))
    for j in range(sy, ey):
        for k in range(sx, ex):
            graph[j][k] = 1


dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

ans = 0
result = []
for i in range(M):
    for j in range(N):
        size = 0
        if graph[i][j] == 0:
            dfs(i,j)
            result.append(size)
            ans += 1

print(ans)
print(*sorted(result))