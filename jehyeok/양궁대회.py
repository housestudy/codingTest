# 내 답
# 일단 시간 안에 못 풀었다. 백트래킹이라고 아는데까지도 시간이 좀 걸렸고 파이썬 미숙도 좀.. ㅎ...
# 생각한 내용은 백트래킹을 이용해 모든 경우의 수를 확인하는 것이다.
# 처음엔 모든 경우의 수니까 순열로 풀면 되지 않을까.. 했는데 과녁에 몇 개가 꽂혀있는지 몰라서 해당 방식으로는 접근이 불가능했다.
# 그래서 백트래킹을 이용했고, cnt(발사한 화살의 수)에 info[i]+1 을 계속 더해주면서 꽂을수 있는 케이스에 대해서만 작업을 하였다.
# 백트래킹을 하다가 cnt == n이 되면 전체 점수를 구하고, 최고점과 비교해 최고점이 갱신되면 answer도 바꿔주는 식으로 했고
# answer가 빈 배열이라면 즉, 최고점 갱신이 단 한번도 되지 못했으면 -1을 출력하면 되겠다 싶었다.
# 그런데... 망할 파이썬 실력이 발목을 잡는다. 아무리 봐도 70점은 나올거같은데...
# 문제는 못고치겠다 ㅎ 나중에라도 고쳐보는걸로... (누가 고쳐줄사람~)
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]	

def solution(n, info):
    answer = []

    arr = []
    cnt = 0

    def back(cnt):
        if cnt == n:
            tmp = 0
            for k in range(n):
                if k in arr:
                    tmp += (info[k] + 1)
                    print(k, info[k], arr)

            if maxCnt < tmp:
                maxCnt = tmp
                # 여기서 answer만 바꿔주고
                
            return maxCnt
        
        for i in range(n):
            if i not in arr and (cnt + info[i]) < 5:
                arr.append(i)
                cnt += (info[i] + 1)
                back(cnt)
                cnt -= (info[i] + 1)
                arr.pop()

    back(cnt)

    # len(answer) == 0이면 -1, 아니면 해당 answer에 해당하는 index들에만 info[index] + 1값 넣어주고 나머지 0 넣어주면 될거같은데...

    return answer

print(solution(n, info))

# 정답
# 정답이 정말 많다. 백트래킹으로 푼 사람들도 있고 bfs로 푼 사람들도 있고 뭐 다양한 방법이 많다.
# 일단 가져온 정답코드는 bfs

def solution(n, info):
	# 어피치의 총 점수 계산
    apeach = sum([10-i for i in range(10) if info[i]])
    # 과녁의 각 점수별 실질적으로 얻어지는 점수
    score = [(10-i)*2 if info[i] else 10-i for i in range(10)]
    # BFS를 위한 queue. 10점을 쏘지 않은 경우 기본 추가
    queue = [[0]]
    answer = []
    # 10점을 쏠 수 있는 경우, 쏜 경우를 queue에 추가
    if n >= info[0]+1:
        queue.append([info[0]+1])
        
    while queue:
        recent = queue.pop(0)
        # 주어진 화살을 다 쐈거나, 10~1점까지 다 쏜 경우
        if sum(recent) == n or len(recent) == 10:
            new = sum([score[i] for i in range(len(recent)) if recent[i]])
            old = sum([score[i] for i in range(len(answer)) if answer[i]])
            # apeach보다 많은 점수를, 그리고 기존 answer 이상의 점수를 얻었다면 update
            if new > apeach and new >= old:
                answer = recent
        # 아직 덜 쐈는데, 이번 점수에 (어피치+1)을 쏠 수 있다면
        elif sum(recent)+info[len(recent)]+1 <= n:
        	# 쏜 경우, 안 쏜 경우 모두 queue에 append
            queue.append(recent + [info[len(recent)]+1])
            queue.append(recent + [0])
        # 아직 덜 쐈는데, 쏠 화살이 안 남아있다면, 안 쏜 경우만 append
        else :
            queue.append(recent + [0])
    # apeach보다 많은 점수를 낼 수 없다면, [-1] return
    if not answer:
        return [-1]
    # 그렇지 않다면, [answer + 남은 점수 안쏘고 + 0점에 다 쏘기] return
    return answer + [0]*(10 - len(answer)) + [n-sum(answer)]