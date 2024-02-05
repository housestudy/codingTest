n, s, a, b = 7, 3, 4, 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	

INF = 1e9

import heapq

def solution(n, s, a, b, fares):
    answer = INF

    graph = [[] for _ in range(n + 1)]

    for fare in fares:
        u, v, w = fare[0], fare[1], fare[2]
        graph[u].append((v, w))
        graph[v].append((u, w))

    def dijkstra(distance, start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            # 탐색할 노드와 거리를 가져옴
            dist, now = heapq.heappop(q)

            # 기존에 저장된 거리보다 탐색할 노드의 거리가 길면 볼 필요 X
            if distance[now] < dist:
                continue

            for i in graph[now]:
                # dist + i[1] = 해당 노드를 거쳐갈 때 거리
                # 저장된 거리보다 작으면 갱신
                if dist + i[1] < distance[i[0]]:
                    distance[i[0]] = dist + i[1]
                    heapq.heappush(q, (dist + i[1], i[0]))

        return distance

    for i in range(1, n + 1):
        distance_ab = INF
        distance_a = INF
        distance_b = INF

        distance = [INF] * (n + 1)

        # 같이 가기
        distance_ab = dijkstra(distance, s)[i]
        # 같이 가서 a 집까지
        distance_a = dijkstra(distance, i)[a]
        # 같이 가서 b 집까지
        distance_b = dijkstra(distance, i)[b]

        result = distance_a + distance_b + distance_ab

        answer = min(answer, result)

    return answer

print(solution(n, s, a, b, fares))