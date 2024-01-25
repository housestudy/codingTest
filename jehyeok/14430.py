# 내 정답
# 아니 나 너무 bfs로만 가려고 하나..?
# 2차원 배열에서 경로 따라서 어디 가는 문제만 보이면 일단 bfs 박고 보네
# 근데 bfs를 못끊겠는데 ㅋ...

# import sys
# from collections import deque

# def bfs(arr):
#     dx = [1, 0]
#     dy = [0, 1]

#     datas = [(0, 0)]
#     queue = deque(datas)

#     while queue:
#         data = queue.popleft()

#         x = data[0]
#         y = data[1]

#         for i in range(2):
#             nx, ny = x, y

#             while True:
#                 nx += dx[i]
#                 ny += dy[i]

#                 if nx < 0 or ny < 0 or nx >= len(arr) or ny >= len(arr[0]):
#                     nx -= dx[i]
#                     ny -= dy[i]
#                     break

#                 if arr[nx][ny] == 1:
#                     break

#             if arr[nx][ny] == 1:
#                 queue.append((nx, ny))
#                 arr[nx][ny] = arr[x][y] + 1

#     return max(max(arr))

# N, M = map(int, sys.stdin.readline().strip().split())
# arr = []
# for i in range(N):
#     arr.append(list(map(int, sys.stdin.readline().strip().split())))

# print(bfs(arr))

# 정답
# DP 기본문제라네여 ㅎ
N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = li[0][0]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        # j == 0인 상태에서 하향할 경우, 즉 (i, 0) 들에 대해
        elif i > 0 and j == 0:
            dp[i][j] = dp[i - 1][j]
        # i == 0인 상태에서 우향할 경우, 즉 (0, j) 들에 대하여
        elif i == 0 and j > 0:
            dp[i][j] = dp[i][j - 1]
        # 나머지 애들은 본인 상, 좌 중에 더 큰 값을
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # li[i][j] == 0이면 dp에 변화 없을거고 1이면 dp에도 +1 해줌
        dp[i][j] += li[i][j]

print(max(map(max, dp)))