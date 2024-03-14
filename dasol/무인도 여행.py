import sys
sys.setrecursionlimit(10**6)
def solution(maps):
    muindo = []
    answer = []
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for m in maps:
        muindo.append(list(m))
    rows = len(maps)
    cols = len(muindo[0])

    def dfs(x, y):
        food = int(muindo[x][y])
        muindo[x][y] = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < rows and 0 <= ny < cols and muindo[nx][ny] != "X" and muindo[nx][ny] != 0:
                food += dfs(nx, ny)
        return food
        
    for i in range(rows):
        for j in range(cols):
            if muindo[i][j] != "X" and muindo[i][j] != 0:
                answer.append(dfs(i,j))

    answer.sort()
    if answer: return answer
    else: return [-1]