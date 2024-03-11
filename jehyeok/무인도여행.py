from collections import deque

maps = ['XXX', 'XXX', 'XXX']

def bfs(maps, i, j, N, M, visit):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    queue.append((i, j))

    visit[i][j] = 1
    result = int(maps[i][j])

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if  visit[nx][ny] == 0 and maps[nx][ny] != 'X':
                visit[nx][ny] = 1
                result += int(maps[nx][ny])
                queue.append((nx, ny))

    return result

def solution(maps):
    N, M = len(maps), len(maps[0])

    visit = [[0] * M for _ in range(N)]
    answer = []
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X' and visit[i][j] == 0:
                answer.append(bfs(maps, i, j, N, M, visit))
    
    if len(answer) > 0: answer.sort()
    else: answer = [-1]

    return answer

print(solution(maps))