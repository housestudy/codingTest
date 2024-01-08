def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    skill_board = [[0] * (m + 1) for _ in range(n + 1)]

    for s in skill:
        action_type, r1, c1, r2, c2, degree = s
        skill_board[r1][c1] += degree if action_type == 2 else -degree
        skill_board[r1][c2 + 1] += -degree if action_type == 2 else degree
        skill_board[r2 + 1][c2 + 1] += degree if action_type == 2 else -degree
        skill_board[r2 + 1][c1] += -degree if action_type == 2 else degree

    for row in range(n):
        for column in range(m):
            skill_board[row][column + 1] += skill_board[row][column]

    for column in range(m):
        for row in range(n):
            skill_board[row + 1][column] += skill_board[row][column]
    for row in range(n):
        for column in range(m):
            if board[row][column] + skill_board[row][column] > 0:
                answer += 1
    return answer