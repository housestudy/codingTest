# 내 답
# 아니 예시도 하나밖에 없고 뭔데요
# 누가봐도 다익스트라잖아
import heapq
import sys
input = sys.stdin.readline

INF = 1e9

N, E = map(int, input().strip().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().strip().split())

def dijkstra(distance, start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                if dist + i[1] < distance[i[0]]:
                    distance[i[0]] = dist + i[1]
                    heapq.heappush(q, (dist + i[1], i[0]))

        return distance

distance_v1 = INF
distance_v2 = INF
distance_N = INF

distance = [INF] * (N + 1)

# 1 -> v1 -> v2 -> N
# 1부터 v1까지
distance_v1 = dijkstra(distance, 1)[v1]
# v1부터 v2까지
distance_v2 = dijkstra(distance, v1)[v2]
# v2부터 N까지
distance_N = dijkstra(distance, v2)[N]
answer1 = distance_v1 + distance_v2 + distance_N

distance_v1 = INF
distance_v2 = INF
distance_N = INF

# 1 -> v2 -> v1 -> N
# 1부터 v2까지
distance_v2 = dijkstra(distance, 1)[v2]
# v2부터 v1까지
distance_v1 = dijkstra(distance, v2)[v1]
# v1부터 N까지
distance_N = dijkstra(distance, v1)[N]
answer2 = distance_v1 + distance_v2 + distance_N

answer = min(answer1, answer2)

if answer >= INF: answer = -1

print(answer)

# 정답
# ...? 뭐가 다른데요...
v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))


def dijkstra(start):
    distance = [INF] * (v + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    # 반환값은 최단 거리 배열
    return distance


v1, v2 = map(int, input().split())

# 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[v]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[v]

result = min(v1_path, v2_path)
print(result if result < INF else -1)