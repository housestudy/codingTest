from collections import deque

def solution(land):
    answer = 0
    row = len(land)
    col = len(land[0])
    dp = [0 for _ in range(col)]
    def bfs(i,j):
        dx, dy = [-1, 1, 0, 0] , [0, 0, -1, 1]
        size = 0
        left = j
        right = j
        land[i][j] = 0
        q = deque([[i,j]])

        while q:
            x, y = q.popleft()
            size += 1
            for i in range(4):
                nx , ny = x +dx[i], y + dy[i]
                if 0 <= nx < row and 0 <= ny < col :
                    if land[nx][ny] == 1 :
                        land[nx][ny] = 0
                        q.append([nx,ny])
                        if ny < left :
                            left = ny
                        if ny > right:
                            right = ny
        return size, left, right

    for i in range(col):
        for j in range(row):
            if land[j][i] == 1:
                size, left, right = bfs(j,i)
                for k in range(left, right + 1):
                    dp[k] += size

    

    answer = max(dp)
    return answer