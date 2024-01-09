# 누적합 문제이다.
# 1차원 배열로 누적합 예시를 들어보면
# [0, 0, 0, 0, 0, 0] 인 배열이 있을 때
# 0~2번 인덱스까지 N만큼 빼고 싶다면 첫번째인 0번 인덱스에 -N을 해주고 마지막 + 1번 인덱스인 3번 인덱스에 + N을 해준다.
# [-N, 0, 0, N, 0, 0]이 되는 것이다.
# 이 상태에서 누적합을 하게 되면 [-N, -N, -N, 0, 0, 0] 이 되어 0~2번 인덱스까지 N만큼 뺀 것이 된다.

# 만약 0~2번째는 N만큼 감소시키고 1~3번째는 M 만큼 감소시킨다고 생각해보면
# [-N, -M, 0, M, N, 0]이 될 것이고
# 누적합을 사용하면 [-N, -M-N, -M-N, -M, 0, 0] 이 되게 된다.

# 이렇게 된다면 누적합을 기록하는 배열에 값을 저장한 후 마지막에 한번만 누적합을 계산해 배열과 더하면 되므로 
# O(1)의 시간복잡도를 가지게 된다.

# 2차원 배열에서도 마찬가지로 작업한다.
# (1, 1) ~ (3, 3)까지 N만큼 뺀다고 생각하면 (1, 1), (4, 4)에 -N, (1, 4), (4, 1)에 +N을 해준다.
# 이후 행 기준으로 누적합을 진행하고 이후 열 기준으로 누적합을 진행하면 끝

# 누적합 공부 전 내 코드
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

# 정답
def solution(board, skill):
    answer = 0
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)] # 누적합 기록 배열

    # 누적합 기록
    # 이게 한 번에 되는건가 싶을수는 있는데
    # 위에서도 예시를 들었듯이 0~2까지는 -N, 1~3까지는 -M 이라고 해도
    # 그냥 공식대로 해놓고 누적합 하면 답이 나온다.
    for type, r1, c1, r2, c2, degree in skill:
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2 + 1] += -degree if type == 2 else degree
        tmp[r2 + 1][c1] += -degree if type == 2 else degree
        tmp[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    # 행 기준 누적합
    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i][j + 1] += tmp[i][j]

    # 열 기준 누적합
    for i in range(len(tmp[0]) - 1):
        for j in range(len(tmp) - 1):
            tmp[i + 1][j] += tmp[i][j]

    # 기존 배열과 합
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += tmp[i][j]

            if board[i][j] > 0: answer += 1

    return answer