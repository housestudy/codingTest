# 골드 4
# 플로이드 워셜 공부한 기념
import sys

INF = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

# 그냥 플로이드 워셜인 줄 알았더니
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = min(c, graph[a][b]) # 노선이 하나가 아닐 수도 있네...

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if graph[a][b] == 1e9:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")

    print()