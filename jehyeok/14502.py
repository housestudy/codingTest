# 백준 14502

# 내 정답
# 오늘은 코테... 질려서 잘하는 bfs 문제로 ㅎ...
import sys
from collections import deque
from copy import deepcopy
from itertools import combinations

N, M = map(int, sys.stdin.readline().strip().split())

maps = []
zeros = []
viruses = []

for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().strip().split())))

    for j in range(M):
        if maps[i][j] == 0:
            zeros.append((i, j))
        if maps[i][j] == 2:
            viruses.append((i, j))

zeros = list(combinations(zeros, 3))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(tmp_map, x, y):
    datas = [(x, y)]
    queue = deque(datas)
    
    while queue:
        data = queue.popleft()

        x = data[0]
        y = data[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if tmp_map[nx][ny] == 0:
                queue.append((nx, ny))
                tmp_map[nx][ny] = 2

    return tmp_map

sizes = []

for zero in zeros:
    tmp_map = deepcopy(maps)

    for data in zero:
        tmp_map[data[0]][data[1]] = 1

    for virus in viruses:
        tmp_map = bfs(tmp_map, virus[0], virus[1])

    size = 0

    for i in range(N):
        for j in range(M):
            if tmp_map[i][j] == 0:
                size += 1

    sizes.append(size)

print(max(sizes))