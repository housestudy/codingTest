def solution(board, skill):
    # length_skill = len(skill)
    row_board = len(board)
    col_board = len(board[0])
    answer = row_board * col_board

    total_damage = [[0 for _ in range(col_board) ] for _ in range(row_board) ]

    for type, r1, c1, r2, c2, degree in skill:
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                # 토탈 데미지 계산하기
                if type == 1:
                    total_damage[i][j] -= degree
                else:
                    total_damage[i][j] += degree

                # 직접 매번 수정하기
                # temp = board[i][j]
                # if type == 1: # 적의 공격
                #     if temp > 0 :
                #         if temp <= degree:
                #             answer -= 1
                #     board[i][j] -= degree
                # else: # 회복
                #     if temp <= 0:
                #         if abs(temp) < degree:
                #             answer += 1
                #     board[i][j] += degree
    
    for i in range(row_board):
        for j in range(col_board):
            if total_damage[i][j] < 0 and abs(total_damage[i][j]) > board[i][j]:
                answer -=1
    
        
    return answer