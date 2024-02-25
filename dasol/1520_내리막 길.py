import sys

#dfs랑 dp콜라보 문제
input = sys.stdin.readline

M, N = map(int, input().split())
mountain = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dp= [[0]*N for _ in range(M)]

for i in range(M):
    mountain.append(list(map(int, input().split())))

def count(x, y):
    v = mountain[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= ny <N and 0<= nx < M and mountain[nx][ny] < v:
            if dp[nx][ny] != 0:
                dp[nx][ny] += 1
            else: 
                dp[nx][ny] = dp[x][y]
            count(nx,ny)

dp[0][0] = 1
count(0, 0)
print(dp[M-1][N-1])