from collections import deque


def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])

    def bfs(a, b, lever, num, exit_x, exit_y):
        print('a,b:',a,b)
        print('lever:',lever)
        INF = int(1e9)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        board = [[INF] * m for _ in range(n)]
        board[a][b] = num
        queue = deque()
        queue.append([a, b])

        while queue:
            print('queue:',queue)
            print('board:',board)
            x, y = queue.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue

                if maps[nx][ny] == 'X':
                    continue

                if maps[nx][ny] == 'L' and lever == False:
                    board[nx][ny] = min(board[nx][ny], board[x][y] + 1)
                    lever = True
                    return nx,ny,lever,board[nx][ny]

                elif maps[nx][ny] == 'E' and lever == True:
                    board[nx][ny] = min(board[nx][ny], board[x][y] + 1)

                elif board[nx][ny] != min(board[nx][ny], board[x][y] + 1):
                    board[nx][ny] = min(board[nx][ny], board[x][y] + 1)
                    queue.append([nx, ny])
                else:
                    continue
        return exit_x,exit_y,lever, board[exit_x][exit_y]

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start_x = i
                start_y = j
            elif maps[i][j] == 'E':
                exit_x = i
                exit_y = j

    next_x,next_y,lever,num = bfs(start_x, start_y, False, 0, exit_x, exit_y)
    print('next_x,next_y,num:',next_x,next_y,num)
    print('lever', lever)
    exit_x, exit_y,lever,answer = bfs(next_x,next_y,lever,num, exit_x, exit_y)
    print('lever',lever)
    if lever == False or answer == -1:
        return -1
    else:
        return answer

maps = 	["SXXOX", "EXXXL", "OOXOO", "OXXXX", "OOOOO"]
result = solution(maps)
print(result)
SXXOX
EXXXL
OOXOO
OXXXX
OOOOO