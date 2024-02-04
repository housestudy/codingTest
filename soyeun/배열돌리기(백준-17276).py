from copy import deepcopy

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = [[0]*n for j in range(n)]

    if d < 0:
        d += 360
    if d == 360 or 0:
        for temp_graph in graph:
            print(*temp_graph)
    else:
        for i in range(d//45):
            for row in range(n):
                for column in range(n):
                    if row == column:
                        result[row][column] = graph[n//2][column]
                    elif row == n//2:
                        result[row][column] = graph[n-column-1][column]
                    elif row + column == n-1:
                        result[row][column] = graph[row][n//2]
                    elif column == n//2:
                        result[row][column] = graph[row][row]
                    else:
                        result[row][column] = graph[row][column]
            graph = deepcopy(result)
        for temp_graph in graph:
            print(*temp_graph)

















# 이건 말이 안 됨
# 거의 하드코딩
# 고정된 좌표가 있음 => ch리스트를 이용하여 고정시키기
# 시계 방향
# (열 기준) n//2를 기준으로 왼쪽에 있으면 위로 올리기
# 위로 이동하지 못할 경우 한 칸 더 위로 이동. 이 때, 한 칸 더 위로 이동하지 못할 경우 오른쪽으로 이동
# n//2를 기준으로 오른쪽에 있으면 아래로 이동
# 아래로 이동하지 못 할 경우 한 칸 더 아래로 이동. 이 때, 한 칸 더 아래로 이동하지 못할 경우 왼쪽으로 이동
# 열이 n//2 인 경우 행이 n//2보다 작거나 큰 경우로 나눠서 해결
# 반시계 방향은 시계 방향 반대로 구성

# def clockwise(n, graph):
#     result = [[0] * n for _ in range(n)]
#     for row in range(n):
#         for column in range(n):
#             if column < n//2:
#                 if ch[row][column] == 0:
#                     result[row][column] = graph[row][column]
#                 elif row-1 > 0:
#                     if ch[row-1][column] == 1:
#                         result[row-1][column] = graph[row][column]
#                     elif ch[row-1][column] == 0:
#                         result[row-2][column] = graph[row][column]
#                 elif row-1 < 0:
#                     if ch[row][column+1] == 1:
#                         result[row][column+1] = graph[row][column]
#                     elif ch[row][column+1] == 0:
#                         result[row][column+2] = graph[row][column]
#
#             elif column > n//2:
#                 if ch[row][column] == 0:
#                     result[row][column] = graph[row][column]
#                 elif row+1 < n:
#                     if ch[row+1][column] == 1:
#                         result[row+1][column] = graph[row][column]
#                     elif ch[row+1][column] == 0:
#                         result[row+2][column] = graph[row][column]
#                 elif row+1 > n:
#                     if ch[row][column-1] == 1:
#                         result[row][column-1] = graph[row][column]
#                     elif ch[row][column-1] == 0:
#                         result[row][column-2] = graph[row][column]
#             else:
#                 if row < n//2:
#                     result[row][column+1] = graph[row][column]
#                 elif row > n//2:
#                     result[row][column-1] = graph[row][column]
#                 else:
#                     result[row][column] = graph[row][column]
#     return result
#
# t = int(input())
#
# for _ in range(t):
#     ch = [[1,0,1,0,1],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[1,0,1,0,1]]
#     n, d = map(int, input().split())
#     # d가 양수이면 시계방향, 음수이면 반시계방향
#     graph = [list(map(int,input().split()))for _ in range(n)]
#     if d > 0:
#         for i in range(d//45):
#             answer = clockwise(n, graph)
