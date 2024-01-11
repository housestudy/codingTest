# https://school.programmers.co.kr/learn/courses/30/lessons/250136
# Lv2. PCCP 기출

# 내 생각
# bfs 같다.
# 각 열에 대해서 시추관을 뚫었다고 가정한 이후
# (N, 0) 부터 한 칸씩 내려가면서 석유가 있는 공간이면 bfs를 진행한다.
# 그 중 가장 많이 석유를 뽑을 수 있는 케이스를 고르면 될듯

# 근데 해보니... 답도 틀리긴 했는데 효율성도 개나 갖다 줘버렸다

from collections import deque
from copy import deepcopy

land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(land, x, y):
    datas = [(x, y)]
    queue = deque(datas)

    cnt = 0

    while queue:
        data = queue.popleft()

        x = data[0]
        y = data[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= len(land) or ny >= len(land[0]):
                continue

            if land[nx][ny] == 0:
                continue

            if land[nx][ny] == 1:
                queue.append((nx, ny))
                land[nx][ny] = 2
                cnt += 1

    return (cnt, land)

def solution(land):
    answer = 0

    for i in range(len(land[0])):
        cnt = 0
        tmp_land = deepcopy(land)

        for j in range(len(land)):
            if land[j][i] == 1:
                bfs_result = bfs(tmp_land, j, i)
                cnt += bfs_result[0]
                tmp_land = bfs_result[1]

        if answer < cnt:
            answer = cnt

    return answer

print(solution(land))


# 정답
def solution(land):
    answer = 0

    n = len(land)
    m = len(land[0])

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    result = [0 for i in range(m+1)]
    visited = [[0 for i in range(m)] for j in range(n)]
    
    def bfs(a, b):
        count = 0
        visited[a][b] = 1

        q = deque()
        q.append((a,b))

        min_y, max_y = b, b

        while q:
            x,y = q.popleft()

            min_y = min(min_y, y)
            max_y = max(max_y, y)

            count += 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue

                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
        
        for i in range(min_y, max_y+1):
            result[i] += count
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i,j)

    answer = max(result)
    
    return answer