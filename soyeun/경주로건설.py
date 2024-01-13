from collections import deque


def solution(board):
    n = len(board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y, cost, d):
        graph = [[0] * n for _ in range(n)]

        for j in range(n):
            for k in range(n):
                if board[j][k] == 1:
                    graph[j][k] = 1

        queue = deque()
        queue.append([x, y, cost, d])

        while queue:
            x, y, cost, idx = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if graph[nx][ny]==1:
                    continue
                if idx == i:
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600

                if graph[nx][ny] == 0 or ((graph[nx][ny] != 0) and (graph[nx][ny] > new_cost)):
                    graph[nx][ny] = new_cost
                    queue.append([nx, ny, new_cost, i])
                else:
                    continue
        return graph[n - 1][n - 1]

    return min(bfs(0, 0, 0, 1), bfs(0, 0, 0, 3))