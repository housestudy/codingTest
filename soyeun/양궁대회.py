from collections import deque

def bfs(n, info):
    result = []
    queue = deque()
    queue.append([0,[0]*11])
    max_score = 0

    while queue:
        score, arrow = queue.popleft()
        if sum(arrow) > n:
            continue
        elif score == 10:
            temp3 = arrow.copy()
            temp3[score] = n-sum(arrow)
            queue.append([score+1,temp3])
        elif sum(arrow) == n:
            lion, apeach = 0, 0
            for i in range(11):
                if arrow[i] > 0 or info[i] > 0:
                    if arrow[i] > info[i]:
                        lion += 10-i
                    else:
                        apeach += 10-i
            if lion > apeach:
                score_diff = lion - apeach
                if score_diff > max_score:
                    max_score = score_diff
                    result = []
                elif score_diff < max_score:
                    continue
                result.append(arrow)
        else:
            temp1 = arrow.copy()
            temp2 = arrow.copy()
            # 라이언이 어피치보다 1발 더 쏘는 경우
            temp1[score] = info[score] + 1
            queue.append([score+1,temp1])
            # 라이언이 해당 점수를 포기(0점)
            temp2[score] = 0
            queue.append([score+1,temp2])
    return result

def solution(n, info):
    answer = bfs(n,info)
    if len(answer) == 0:
        return [-1]

    return answer[-1]

n = 9
info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
print(solution(n,info))
# 1. 라이언이 어피치보다 1발 더 쏘거나 아니면 그 화살을 아꼈다가 다른 점수에 쏘는 경우
# 2. 화살 쏘는 순서는 10점부터 시작
# 3. bfs 종료 조건
# (1) 화살을 다 쏜 경우
# 라이언과 어피치의 점수 계산
# 라이언이 이겼을 경우 최대 점수 확인하고 최대 점수이면 result에 추가
# (2) 마지막 화살을 쏠 차례인데 앞에서 화살을 쏘지 않았을 때(10~2까지 모두 점수를 포기한 경우)
# (3) 화살을 더 쏜 경우