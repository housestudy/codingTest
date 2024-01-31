def solution(n, info):
    # 냅색 문제 + 백트래킹 문제. 냅색 푼지가 너무 오래되서 기억이 전혀 안났음;;
    apeach_score = sum(10-i for i in range(11) if info[i] != 0)
    
    # 어피치가 확보한 점수를 뺏으면 score의 2배를 얻는 것으로 보면 되고,
    # 어피치가 확보하지 못한 점수를 얻으면 score를 얻는 것으로 보면 됩니다.
    # weight는 각 점수 별로 (어피치가 쏜 화살 수+1)로 정의됩니다.
    weights = [-1] + [x+1 for x in info]
    values = [-1] + [2*(10-i) if info[i] != 0 else (10-i) for i in range(11)]
    
    # 냅색 풀이코드
    A = [[0] * (n + 1) for _ in range(12)]
    for i in range(1, 12):
        for w in range(1, n+1):
            if weights[i] > w:
                A[i][w] = A[i-1][w]
            else:
                A[i][w] = max(A[i-1][w-weights[i]] + values[i], A[i-1][w])

    # 오른쪽 끝 점수를 봅니다.
    # 어피치가 획득했던 점수보다 작거나 같으면 비기거나 진다는 뜻입니다.
    final_score = A[-1][-1] - apeach_score
    if final_score <= 0:
        return [-1]
    
    # 백트래킹 해서 각 점수에 화살을 얼마나 쏴야 할지 봅니다.
    answer = [0] * 11
    w = n
    for i in range(11, 0, -1):
        # A[i][w] 값이 A[i-1][w-weights[i]] + values[i]와 같으면
        # i점에 "적어도" weights[i]개의 화살을 쐈다는 것입니다.
        if A[i][w] == A[i-1][w-weights[i]] + values[i]:
            answer[i-1] = weights[i]
            w = w-weights[i]
    
    answer[-1] += (n - sum(answer))
    return answer