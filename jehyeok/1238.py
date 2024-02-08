import sys
import heapq

INF = int(1e9)

N, M, X = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N + 1)]
graph_for_reverse = [[] for _ in range(N + 1)]

distance = [INF] * (N + 1)
distance_for_reverse = [INF] * (N + 1)

for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, t))
    graph_for_reverse[b].append((a, t))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def dijkstra_for_reverse(start):
    q = []
    heapq.heappush(q, (0, start))
    distance_for_reverse[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance_for_reverse[now] < dist:
            continue

        for i in graph_for_reverse[now]:
            cost = dist + i[1]
            if cost < distance_for_reverse[i[0]]:
                distance_for_reverse[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(X) # 실제 그래프에서 x에서 각각으로 가는 거리
dijkstra_for_reverse(X) # 반대로 뒤집었으니 각각에서 x 로 가는 거리가 들어감

result = [distance[x] + distance_for_reverse[x] for x in range(1, N + 1)]

print(max(result))