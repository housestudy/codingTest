# bfs 방식은 시간 초과
# from collections import deque
# n,m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# ch = [[0]*m for _ in range(n)]
# result = 0
# queue = deque()
# queue.append([0,0])
#
# while queue:
#     x, y = queue.popleft()
#     ny = y + 1
#     if ny >= 0 and ny < m:
#         if graph[x][ny] == 1:
#             ch[x][ny] = ch[x][y]+1
#             result = max(result, ch[x][ny])
#         queue.append([x, ny])
#     nx = x + 1
#     if nx >= 0 and nx < n:
#         if graph[nx][y] == 1:
#             ch[nx][y] = ch[x][y] + 1
#             result = max(result, ch[nx][y])
#         queue.append([nx, y])
# print(result)

#dp
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
result = 0
dp[0][0] = graph[0][0]

for row in range(n):
    for column in range(m):
        if row == 0 and column == 0:
            continue
        elif row == 0 and column > 0:
            dp[row][column] += dp[row][column-1]
        elif row > 0 and column == 0:
            dp[row][column] += dp[row-1][column]
        else:
            dp[row][column] += max(dp[row-1][column],dp[row][column-1])
        if graph[row][column] == 1:
            dp[row][column] += 1
        #result = max(result, dp[row][column])
print(max(map(max,dp)))








