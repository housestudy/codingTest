# 난 그래프탐색이 왜 이렇게 좋은지~
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())

graph = []
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

for i in range(N):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque([(x, y, z)])

    while queue:
        x, y, z = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))

            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

    return -1

print(bfs(0, 0, 0))