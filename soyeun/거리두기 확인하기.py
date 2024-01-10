from collections import deque


def bfs(places,k):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(5):
        for j in range(5):
            queue = deque()
            if places[k][i][j] == 'P':
                visited = [[0] * 6 for _ in range(7)]
                queue.append((i,j))
                visited[i][j] = 1
                while queue:
                    x, y = queue.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                            continue
                        if visited[nx][ny]:
                            continue
                        if places[k][nx][ny] == 'X' or visited[x][y] >= 3:
                            continue
                        if places[k][nx][ny] == 'P':
                            return 0
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
    return 1


def solution(places):
    answer = []
    for k in range(5):
        answer.append(bfs(places,k))
    return answer