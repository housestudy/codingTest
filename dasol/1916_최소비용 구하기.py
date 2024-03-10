# import sys
# from collections import deque

# def bfs(a):
#     q = deque()
#     q.append([a,0])

#     while q:
#         x = q.popleft()

#         if distance[x[0]] < x[1]:
#             continue

#         for i in route[x[0]]:
#             # if visited[i] == False:
#             # visited[i] = True
#             if distance[i[0]] > distance[x] + i[1]:
#                 distance[i[0]] = distance[x] + i[1]
#                 q.append([i[0],distance[i[0]]])



# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# route = [[] for asdf in range(n+1)]
# visited = [False] * (n + 1)
# distance = [1e5] * (n+1)

# for i in range(m):
#     x, y, c = map(int, input().split()) # x는 출발점, y는 도착점 c는 드는 최소 비용
#     route[x].append((y,c))

# a, b= map(int, input().split()) #a에서 출발해서 b로 갈때의 최소 비용

# distance[a] = 0
# bfs(a)

# print(distance[b])



import sys
import heapq

def bfs():
    heap = []
    heapq.heappush(heap, [start, 0])
    visitcost[start] = 0

    while heap:
        x, y = heapq.heappop(heap)

        if visitcost[x] < y :
            continue
        
        for i, j in graph[x]:
            temp = y + j
            if temp < visitcost[i]:
                visitcost[i] = temp
                heapq.heappush(heap, [i,temp])

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 2차원 그래프로 표현
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

start, end = map(int, sys.stdin.readline().split()) # 출발 도시와 도착 도시
INF = sys.maxsize
visitcost = [INF] * (n + 1)
bfs() # bfs 탐색

# 도착 도시까지 가는데 드는 최소 비용 출력
print(visitcost[end])