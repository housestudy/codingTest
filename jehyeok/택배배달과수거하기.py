cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries.reverse()
    pickups.reverse()

    while len([x for x in deliveries if x == 0]) != n or len([x for x in pickups if x == 0]) != n:
        give = cap
        get = cap

        # 배달, 수거 중 어쨌든 제일 idx가 높은 곳까지는 가야되므로
        startIdx = 1e9

        for i, d in enumerate(deliveries):
            if d != 0:
                startIdx = min(i, startIdx)
                break
        
        for i, p in enumerate(pickups):
            if p != 0:
                startIdx = min(i, startIdx)
                break

        # 배달부터 해야 트럭이 비어짐
        # 배달
        for i in range(startIdx, n):
            if deliveries[i] < give:
                deliveries[i] = 0
                give -= deliveries[i]
            else:
                deliveries[i] -= give
                give = 0
                break

        # 수거
        for i in range(startIdx, n):
            if pickups[i] < get:
                pickups[i] = 0
                get -= pickups[i]
            else:
                pickups[i] -= get
                get = 0
                break

        answer += (2 * (n - startIdx))

    return answer

print(solution(cap, n, deliveries, pickups))

# 정답
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver = 0   # 남은 배달 가능 개수
    pick = 0   # 남은 수거 가능 개수

    # 무조건 맨 뒤부터 배달, 수거하는게 좋음
    for i in range(n - 1, -1, -1):
        cnt = 0 # 몇번 i번째 집에 왔다갔다 해야되는지
        
        # 남은 배달 가능 개수 < i번째 집에 배달해야 할 개수 이거나
        # 남은 수거 가능 개수 < i번째 집에서 수거해야 할 개수
        # 즉, i번째 집의 배달, 수거를 모두 못 끝낼경우 끝낼 수 있을 때까지
        while deliver < deliveries[i] or pick < pickups[i]:
            cnt += 1
            # 여기가 중요한데 일단 + cap을 박아놨으므로
            # deliver, pick 이 deliveries[i], pickups[i] 보다 작아질 경우는
            deliver += cap
            pick += cap

        # 여기서 i번째 deliveries나 pickups를 계속 제거해 나가다가 조건이 맞을 경우밖에 없음
        deliver -= deliveries[i]
        pick -= pickups[i]
        answer += (i + 1) * cnt

    # 왔다 갔다니까 * 2
    return answer * 2
