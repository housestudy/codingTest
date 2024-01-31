import sys
input = sys.stdin.readline

# dfs로 구현하니까 메모리 초과됐다. 왜 메모리 초과됐는지는 여전히 의문. for문 생성한 상태에서 recursion 이 깊어져서 그런 것 같기도?

n = int(input())
m = int(input())

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
pingping = [[0 for _ in range(n)] for _ in range(n)]
start = n**2
target = []

def dfs(x, y, start, dir):
    while start != 0:
        pingping[x][y] = start
        if start == m:
            target.append(x+1)
            target.append(y+1)
        start -= 1
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n and pingping[nx][ny] == 0 :
            x = nx
            y = ny
        else:
            for newDir in range(4):
                nx = x + dx[newDir]
                ny = y + dy[newDir]
                if 0 <= nx < n and 0 <= ny < n and pingping[nx][ny] == 0 :
                    x = nx
                    y = ny
                    dir = newDir
                    break

dfs(0,0, start, 0)

for i in range(n):
    print(*pingping[i])
print(*target)