# 다익스트라 vs 플로이드 워셜
# 다익스트라 : 시작점으로부터 나머지 정점까지 최단거리를 구할 때
# 플로이드 워셜 : 각 정점간 최단경로를 구할 때
# 다익스트라
# 1. 출발 노드 설정
# 2. 출발 노드를 기준으로 각 노드의 최소 비용을 저장
# 3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드 선택
# 4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용 갱신
# 5. 3~4번 반복

# 다익스트라
import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
i = int(input())
INF = 1e9
graph = [[] for _ in range(v+1)]

for _ in range(e):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

distance = [INF]*(v+1)

queue = []

def dijkstra(i):
    distance[i] = 0
    heapq.heappush(queue,(0,i))
    while queue:
        # heap을 이용하여 pop하면 가장 작은 값부터 나오므로
        dist, now_node = heapq.heappop(queue)

        for node, weight in graph[now_node]:
            cost = dist + weight

            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(queue, (cost, node))

dijkstra(i)

for j in distance[1:]:
    if j == INF:
        print('INF')
    else:
        print(j)

# 플로이드 워셜 풀이의 경우 메모리 초과가 발생
# v, e = map(int, input().split())
# i = int(input())
# INF = 1e9
# graph = [[INF]*v for _ in range(v)]
#
# for _ in range(e):
#     start, end, cost = map(int, input().split())
#     graph[start-1][end-1] = cost
#
# for row in range(v):
#     graph[row][row] = 0
#
# for j in range(v):
#     for k in range(v):
#         for t in range(v):
#             graph[k][t] = min(graph[k][t], graph[k][j]+graph[j][t])
# result = ['INF' if num == INF else num for num in graph[i-1]]
#
# for res in result:
#     print(res)