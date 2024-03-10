# n//2 부터 시작하여 상 오 하 왼 방향으로 이동
# 이 때, 시작하는 행과 열에서 각각 +1 또는 -1한 값까지 가야함
# 상 = 하+1
# 오 = 왼 + 1
# 하 = 상+1
# 왼 = 오 + 1

n = int(input())
m = int(input())

graph = [[0]*n for _ in range(n)]
# 상 오 하 왼
dx = [-1,0,1,0]
dy = [0,1,0,-1]
direction = [0,0,0,0]

x, y = n//2, n//2
graph[x][y] = 1

direction_index = 0

while True:
    index = direction_index % 4
    direction[index] = direction[(direction_index + 2) % 4] + 1
    cnt = direction[index]
    for i in range(cnt):
        if graph[x][y] == m:
            answer = [x+1,y+1]
        nx = x + dx[index]
        ny = y + dy[index]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            break
        graph[nx][ny] = graph[x][y] + 1

        x = nx
        y = ny
    direction_index += 1

    if graph[0][0] == n ** 2:
        break

for row in graph:
    for num in row:
        print(num, end=' ')
    print()

for ans in answer:
    print(ans, end=' ')

