import sys

input = sys.stdin.readline
R, C = map(int, input().split())
boards = []
visited = set()
answer = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(R):
    boards.append(list(input().rstrip()))
# set로 접근하는 것은 나쁘지 않으나, 최대 경로가 아닌 경우에는 다시 거꾸로 진행했을 때 제거해줄 필요가 있다.
# 백트랙킹 기법으로 접근해보자.
def sol(x, y, cnt):
    global answer
    tmp = cnt
    tmp += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and boards[nx][ny] not in visited:
            visited.add(boards[nx][ny])
            sol(nx, ny, tmp)
            visited.discard(boards[nx][ny])
        else:
            if answer < tmp :
                answer = tmp
    return
visited.add(boards[0][0])
sol(0, 0, 0)
print(answer)