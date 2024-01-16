# https://school.programmers.co.kr/learn/courses/30/lessons/176962
# Lv2.

# 내 정답
# 구현..같은데... 그 프로세스 스케줄러 내용 중에 선점형 스케줄러 내용 중 하나인듯?
# 쨌든 내용에 FIFO 개념이 있으니 Queue 쓰는 구현 문제 같아서 풀었으나 ㅎ
# 테스트도 통과 못했다.
# 시간이 너무 오래 걸렸다... 시간만 있어도 풀었을거같은데 구현이라
from collections import deque

plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]

def solution(plans):
    answer = []

    tmp_plans = []

    for plan in plans:
        strStartTime = plan[1].split(':')
        name, startTime, remainTime = plan[0], (int(strStartTime[0]) * 60) + int(strStartTime[1]), int(plan[2])
        tmp_plans.append([name, startTime, remainTime])

    plans = tmp_plans
    # 시작 시간이 빠른 순대로 정렬
    plans = sorted(plans, key=lambda x: x[1])

    # Ready Queue와 Execute Queue를 만들기
    readyQue = deque(plans)
    stoppedQue = deque([])

    while len(answer) != len(plans):
        execute = readyQue.popleft()
        name, startTime, remainTime = execute[0], execute[1], execute[2]

        if len(readyQue) > 0:
            nextPlan = readyQue[0]
            nextStartTime = nextPlan[1]

            # 다 끝냈을 때
            if startTime + remainTime <= nextStartTime:
                answer.append(name)

                # 다음 시작 시간이 됐을 때...는 작업할 필요 없어보이고
                if startTime + remainTime == nextStartTime:
                    continue
                # 아직 다음 시작시간이 안됐을 때
                else:
                    emptyTime = nextStartTime - startTime - remainTime

                    if len(stoppedQue) > 0:
                        while True:
                            if len(stoppedQue) <= 0:
                                break

                            stoppedPlan = stoppedQue.popleft()
                            # 정지된 계획의 남은 시간 < 다음 시작까지 남은 시간
                            if stoppedPlan[1] <= emptyTime:
                                answer.append(stoppedPlan[0])
                                emptyTime -= stoppedPlan[1]
                            else:
                                stoppedQue.append([stoppedPlan[0], stoppedPlan[1] - emptyTime])
                                emptyTime = 0
                                break

            # 다 못 끝냈을 때
            else:
                remainTime = nextStartTime - startTime
                stoppedQue.append([name, remainTime])
        else:
            answer.append(name)

    return answer

print(solution(plans))

# 라고 생각했는데 정답 보니 문제 이해 자체를 잘못했네
# 멈춰있던 문제를 푸는거라 어떤 과제를 다 못끝내도 끝으로 보내는게 아니라 다시 그 과제부터 하는거구나 썩을
# 헛짓거리 했다!
def solution(plans):
    answer = []

    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        st = h * 60 + m
        plans[i][1] = st
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key=lambda x:x[1])
    stack = []

    for i in range(len(plans)):
        if i == len(plans) - 1:
            stack.append(plans[i])
            break
        
        sub, st, t = plans[i]
        nsub, nst, nt = plans[i+1]

        if st + t <= nst:
            answer.append(sub)
            temp_time = nst - (st+t)
            
            while temp_time != 0 and stack:
                tsub, tst, tt = stack.pop()
                if temp_time >= tt:
                    answer.append(tsub)
                    temp_time -= tt
                else:
                    stack.append([tsub, tst, tt - temp_time])
                    temp_time = 0
            
        else:
            plans[i][2] = t - (nst - st)
            stack.append(plans[i])
        
    while stack:
        sub, st, tt = stack.pop()
        answer.append(sub)

    return answer