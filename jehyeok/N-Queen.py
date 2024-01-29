# https://www.acmicpc.net/problem/9663

# 내 정답
# ㅋㅋ... 이게 맞을리가 없지...
# 그래도 N이 작고 시간 제한이 10초니까 이런 식으로 백트래킹이 가나 했는데 개뿔이
N = int(input())

board = [[0] * N for _ in range(N)]
arr = []

answer = 0

def setBoard(board, i, j):
    for k in range(N):
        board[k][j] = 1
        board[i][k] = 1
    
    # 좌상
    t = 0
    while True:
        if i - t == -1 or j - t == -1:
            break
        board[i - t][j - t] = 1
        t += 1
    
    # 우하
    t = 0
    while True:
        if i + t == N or j + t == N:
            break
        board[i + t][j + t] = 1
        t += 1
    
    # 우상
    t = 0
    while True:
        if i - t == -1 or j + t == N:
            break
        board[i - t][j + t] = 1
        t += 1
    
    # 좌하
    t = 0
    while True:
        if i + t == N or j - t == -1:
            break
        board[i + t][j - t] = 1
        t += 1

    return board

def back(board, answer):
    if len(arr) == N:
        answer += 1
        return
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                setBoard(board, i, j)

                arr.append((i, j))
                back(board, answer)
                arr.pop()

                board = [[0] * N for _ in range(N)]
                for data in arr:
                    x, y = data[0], data[1]
                    setBoard(board, x, y)


back(board, answer)
print(answer)

# 답
n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)