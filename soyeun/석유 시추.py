from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    land_ch = [[0]*m for _ in range(n)]
    answer = [0]*m

    def bfs(row, column):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        queue = deque()
        queue.append([row,column])
        land_ch[row][column] = 1
        cnt = 1
        column_ch = set()

        while queue:
            x, y = queue.popleft()
            column_ch.add(y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if land[nx][ny] == 0:
                    continue
                if land_ch[nx][ny] == 0 and land[nx][ny] == 1:
                    queue.append([nx,ny])
                    cnt += 1
                    land_ch[nx][ny] = 1
        return cnt, column_ch


    for row in range(n):
        for column in range(m):
            if land_ch[row][column] == 0 and land[row][column] == 1:
                cnt,column_list = bfs(row, column)
                for j in column_list:
                    answer[j] += cnt
    return max(answer)

land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
print(solution(land))

