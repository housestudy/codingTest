# https://school.programmers.co.kr/learn/courses/30/lessons/118668
# Lv3. 2022 카카오

# 가장 효율이 잘 나오는 문제만 풀어제껴야 된다...
# 무한 루프 돌면서
# 현재 상태에서 풀 수 있는 문제들 리스트 만들고
# 그 중에서 알고력, 코딩력 중 효율이 제일 잘 나오는 문제 하나를 찾고 해당 문제를 푼다.
# 그러다 원하는 결과가 나오면 시간을 출력한다.

alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
# [알고력, 코딩력, 문제를 풀었을때 증가하는 알고력, 문제를 풀었을때 증가하는 코딩력, 푸는데 드는 시간]

def solution(alp, cop, problems):
    answer = 0

    currentAlp = alp
    currentCop = cop

    # 목표치
    wantedAlp = sorted(problems, key=lambda x: x[0], reverse=True)[0][0]
    wantedCop = sorted(problems, key=lambda x: x[1], reverse=True)[0][1]

    while True:
        canSolvedProblems = []

        # 현재 풀 수 있는 문제 리스트 만들고 (대신 둘 중 하나라도 효율이 1 이상)
        for i in range(len(problems)):
            x = problems[i]

            if (x[0] <= currentAlp and x[1] <= currentCop) and (x[2]/x[4] > 1 or x[3]/x[4] > 1):
                tmp = x
                tmp.append(x[2]/x[4])
                tmp.append(x[3]/x[4])
                
                canSolvedProblems.append(tmp)

        # 만약 효율이 1 이상인게 하나도 없으면
        if len(canSolvedProblems) == 0:
            # 코딩력이나 알고력 중 하나를 1만큼 올려야되는데...
            answer += 5
            currentAlp += 5
        # else 인 경우, 효율이 가장 높은거 하나만큼 올린다.    
        else:
            canSolvedProblems = sorted(canSolvedProblems, key=lambda x: max(x[5], x[6]), reverse=True)
            bestItem = canSolvedProblems[0]

            # 알고력 효율이 더 높으면
            if bestItem[5] > bestItem[6]:
                currentAlp += bestItem[2]
            # 코딩력 효율이 더 높으면
            else:
                currentAlp += bestItem[3]
            
            answer += bestItem[4]

        if currentAlp >= wantedAlp and currentCop >= wantedCop:
            break
    
    return answer

print(solution(alp, cop, problems))

# 모르겠다~ 더럽게 어렵네~

# 정답
# DP 문제였다. 예전에 공부할때도 DP를 제일 어려워했는데 ㅋ... 공부 한지 오래돼서 기억도 안나니
# DP 문제인지 조차도 몰라버렸다.
def solution(alp, cop, problems):
    max_alp_req, max_cop_req = [0, 0]  # 목표값
    
    for problem in problems:
        max_alp_req = max(max_alp_req, problem[0])
        max_cop_req = max(max_cop_req, problem[1])
    
    dp = [[float('inf')] * (max_cop_req+1) for _ in range(max_alp_req+1)]
    
    alp = min(alp, max_alp_req)  # 둘중 하나라도 목표값을 넘어가면 안된다.
    cop = min(cop, max_cop_req)
    
    dp[alp][cop] = 0  # dp[i][j]의 의미 : 알고력 i, 코딩력 j을 도달 할 수 있는 최단시간
    
    for i in range(alp, max_alp_req+1):
        for j in range(cop, max_cop_req+1):
            if i < max_alp_req:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop_req:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i+alp_rwd, max_alp_req)  # 둘중 하나라도 목표값을 넘어가면 안된다.
                    new_cop = min(j+cop_rwd, max_cop_req)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
                    
    return dp[max_alp_req][max_cop_req]