import sys

input = sys.stdin.readline

N, M = map(int, input().split())  #N은 세로크기, M은 가로크기

cleanmap = []
cleaned = [[0]*M for asdf in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] #북/동/남/서

r,c,d = map(int, input().split()) #(r,c)는 청소기의 위치 r은 행, c는 열 d는 방향. 시계방향으로 북 0 동 1 남 2 서 3

for i in range(N):
    cleanmap.append(list(map(int, input().split())))

cnt = 1

while True:
    cleaned[r][c] = 1

    tmp = d
    for i in range(4):
        d -= 1
        if d == -1:
            d = 3
        nx = r + dx[d]
        ny = c + dy[d]
        if cleanmap[nx][ny] == 0 and cleaned[nx][ny] == 0:
            r = nx
            c = ny
            cnt += 1
            break
        
    if d == tmp and (r != nx or c != ny):
        nx = r + dx[d-2]
        ny = c + dy[d-2]
        if cleanmap[nx][ny] == 1:
            break
        r = nx
        c = ny

print(cnt)