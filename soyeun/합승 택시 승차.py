# 플로이드와샬
def solution(n, s, a, b, fares):
    INF = 10000000
    answer = INF
    graph = [[INF] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0

    for f in fares:
        node1, node2, fee = f
        graph[node1 - 1][node2 - 1] = fee
        graph[node2 - 1][node1 - 1] = fee

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for t in range(n):
        temp = graph[s - 1][t] + graph[t][a - 1] + graph[t][b - 1]
        answer = min(temp, answer)

    return answer


# 연결된 노드와 비용을 적은 그래프 생성
# 어딘가를 들를때와 들르지 않을 때 비교 후 비용이 더 짧은 것으로 선택
# A와 B의 비용을 각각 구하기
# 노드를 들르는 경로를 각각 저장해놓고 A와 B의 경로가 같은 곳의 비용을 빼기

# bfs로 접근
# 4번에서 시작하여 비용 계산
# a와 b를 동시에 계산 => a와 b를 각각 계산하므로 cost가 2배
# 같이 이동할 경우 cost를 한번 빼주기
# 도착 지점이 a 또는 b 일 때, 플래그를 통해 이 후엔 계산하지 않도록

# 아닌것 같아...dfs 같아...
# start node 부터 시작해서 graph를 통해 연결된 곳으로 이동
# 이 때, 지나간 길을 저장
# 종료 조건 : 도착 지점이 a,b의 집 일 때
from collections import deque

# def bfs(Q,end_node,graph,n):
#     ch = [[0] * (n + 1) for _ in range(n + 1)]
#     total_cost = 0
# 
#     while Q:
#         start, end = Q.popleft()
#         ch[start][end] = 1
#         total_cost += graph[start][end]
#         for i in range(1,n+1):
#             if graph[end][i] > 0 and ch[end][i] == 0:
#                 Q.append([end,i])
# 
# def dfs(graph, end_node, ch, start, end):
#     if end == end_node:
#         return
#     else:
#         if graph[start][end] > 0 and ch[start][end] == 0:
#             cost_cnt += graph[start][end]
#             ch[start][end] = 1
#             for i in range(1, n+1):
#                 if ch[end][i] == 0:
#                     ch[end]
#                     dfs()
# def solution(n, s, a, b, fares):
#     answer = 0
#     graph = [[0]*(n+1) for _ in range(n+1)]





    return answer

n = 6
s = 4
a = 6
b = 1
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]