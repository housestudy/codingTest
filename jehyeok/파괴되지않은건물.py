board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

def solution(board, skill):
    answer = 0

    boardCol = len(board[0])
    boardRow = len(board)
    
    for s in skill:
        type, r1, c1, r2, c2, degree = s[0], s[1], s[2], s[3], s[4], s[5]

        for i in range(boardRow):
            for j in range(boardCol):
                if i >= r1 and i <= r2 and j >= c1 and j <= c2:
                    if type == 1:
                        board[i][j] -= degree
                    else:
                        board[i][j] += degree              

    for i in range(boardRow):
        for j in range(boardCol):
            if board[i][j] > 0:
                answer += 1

    return answer

print(solution(board, skill))