import sys
from collections import deque

# 처음에는 dfs 처럼 접근 했는데, recursionlimit 에 걸림. 무작정 모든 케이스를 전부 수행하면 심히 연산량이 높아짐.
# 최대한 빨리 가는 거니까, bfs처럼 접근해서 불필요한 연산을 줄이는 방식으로 접근함 n과 k는 각각 크기 제한이 있는 점 유의
input = sys.stdin.readline
N, K = map(int, input().split())
load = [sys.maxsize for _ in range(100001)]
load[N] = 0
def sol(s, sec):
    q = deque([[s,sec]])
    while q:
        nx, time = q.popleft()
        if nx == K:
            if load[K] > time:
                load[K] = time
                break
        if 0<= nx*2 < 100001 and load[nx*2] > time:
            load[nx*2] = time
            q.append([nx*2, time])
        if 0<= nx+ 1 < 100001 and load[nx+1] > time + 1:
            load[nx+1] = time + 1
            q.append([nx+1, time+1])
        if 0<= nx-1 < 100001 and load[nx - 1] > time + 1:
            load[nx-1] = time + 1
            q.append([nx-1, time+1])
    return
sol(N, 0)
print(load[K])