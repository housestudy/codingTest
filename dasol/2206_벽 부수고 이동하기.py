import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
dx, dy = [-1, 1, 0, 0], [0,0,-1,1]

# 일반적으로 bfs 문제 혹은 dfs 문제는 주어지는 그래프만 활용해도 visited 를 확인할 수 있는데
# 이 문제에서는 구분해서 해줘야지 단순하게 해결 할 수 있었다.
# 내가 짠 bfs 에서는 이 부분을 해결하기 위해서 조건이 많이 붙었지만 거르지 못하는 케이스가 있었고
# 이 부분은 visited만 사용해도 쉽게 처리할 수 있었다.
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

for i in range(N):
    maze.append(list(map(int, input().rstrip())))

# for i in range(N):
#     for j in range(M):
#         tmp = maze[i][j]
#         maze[i][j] = [tmp, 0] # 각각 False, True로 뚫기 전/후로 나눈 값
# def bfs():
#     q = deque()
#     q.append([0,0,False])
#     while q:
#         x, y, f = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if f == False: #False 인 경우 전부 고려해야 한다.
#                 if 0 <= nx < N and 0 <= ny < M :
#                     if maze[nx][ny][0] == 0:
#                         maze[nx][ny][0] = maze[x][y][0] + 1
#                         q.append([nx, ny, False])
#                     elif maze[nx][ny][0] == 1:
#                         maze[nx][ny][1] = maze[x][y][0] + 1
#                         q.append([nx, ny, True])

#             else: #True인 경우 이미 뚫고 온 것이니, 다시 벽은 뚫으면 안된다.0 이거나 아니면 더 낮은 경우에만 갱신후 q에 삽입
#                 if 0 <= nx < N and 0 <= ny < M and maze[nx][ny][0] != 1:
#                     if maze[nx][ny][1] == 0 :
#                         maze[nx][ny][1] = maze[x][y][1] + 1
#                         q.append([nx, ny, True])
#     return



def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == N - 1 and b == M - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if maze[nx][ny] == 1 and c == 0 :
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif maze[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1


print(bfs(0, 0, 0))