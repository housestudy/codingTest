# 내 답

# 방향성이나 구현하고자 했던건 정확했는데...
# 2가지 문제가 있는데 답 보니까
# 1. 에러 지점을 찾아내지 못했다.
# 2. 코너 설계시 +500원이 아니라 +600원이다..

from collections import deque

board = [[0,0,0],[0,0,0],[0,0,0]]

def solution(board):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    boardSize = len(board)

    def bfs(x, y):
        datas = [(x, y, 0)]
        queue = deque(datas)

        while queue:
            data = queue.popleft()
            x, y, prevDir = data[0], data[1], data[2]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if i == 0 or i == 1:
                    dir = 1
                else:
                    dir = 2

                if nx < 0 or ny < 0 or nx >= boardSize or ny >= boardSize:
                    continue

                if board[nx][ny] == 1:
                    continue

                queue.append((nx, ny, dir))
                
                if prevDir != dir:
                    if x == 0 and y == 0:
                        cost = 100
                    else:
                        # 직선 + 코너를 만드니까
                        cost = 600
                else:
                    cost = 100

                board[nx][ny] = min(board[nx][ny], board[x][y] + cost)

        return board[boardSize - 1][boardSize - 1]

    answer = bfs(0, 0)

    return answer

print(solution(board))

# 정답
def solution(board):
    n = len(board)
    opened = [(0,0,-1,0)] # y, x, direction, cost
    closed = [[-1 for _ in range(n)] for _ in range(n)]
    
    answer = -1
    while opened:
        y, x, d, c = opened.pop(0)
        if (y, x) == (n-1, n-1) and (answer == -1 or answer > c):
            answer = c

        neighbors = [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]
        for direction, (ny, nx) in enumerate(neighbors):            
            # boundary
            if ny <= -1 or ny >= n or nx <= -1 or nx >= n:
                continue
            
            # wall
            if board[ny][nx]:
                continue

            # visited and cheaper
            cost = c + (100 if d == direction or d == -1 else 600)
            if closed[ny][nx] != -1 and closed[ny][nx] < cost:
                continue
                
            opened.append((ny, nx, direction, cost))
            closed[ny][nx] = cost

    return answer