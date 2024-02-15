# 전에 프로그래머스에서 풀었던 바이러스보다 낮은 수준의 그래프 문제

import sys

def dfs(z):
    global count
    if visited[z] == False:
        visited[z] = True
        count += 1
        for i in graph[z]:
            dfs(i)

input = sys.stdin.readline

v = int(input())
e = int(input())

graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
count = -1
# 1번 컴퓨터 부터 시작하므로, 1번 방문 때는 0으로 시작해야만 한다.

for i in range(e):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)
print(count)