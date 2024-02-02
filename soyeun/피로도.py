# 던전의 개수가 1이상 8이하이므로 가능한 순서를 모두 탐색
import itertools

def solution(k, dungeons):
    answer = -1
    dungeons_case = list(itertools.permutations(dungeons,len(dungeons)))
    for case in dungeons_case:
        tired = k
        cnt = 0
        for need, minus in case:
            if tired >= need:
                cnt += 1
                tired -= minus
        answer = max(answer,cnt)
    return answer

k = 80
dungeons = 	[[80,20],[50,40],[30,10]]
print(solution(k,dungeons))