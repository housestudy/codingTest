# 내 답
# 맨날 그래프 탐색을 bfs로만 한 것 같아서 dfs 공부겸 해봤다.
# 덕분에 백준엔 최대 깊이가 있단걸 알았다.
import sys

# 백준 온라인 저지에서 파이썬 재귀 깊이의 최대값이 10^3이라 dfs쓸 땐 이를 10^6으로 늘려줘야 한다고 한다.
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())

    graph = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, sys.stdin.readline().strip().split())
        graph[y][x] = 1

    def dfs(x, y):
        if x <= -1 or y <= -1 or x >= N or y >= M:
            return False

        if graph[x][y] == 1:
            graph[x][y] = 0

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

            return True

        return False

    result = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                if dfs(i, j):
                    result += 1

    print(result)