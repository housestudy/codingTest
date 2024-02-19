# 1. user_id 리스트에서 banned_id에 해당하는 아이디들 구하기 => dict로 저장
# 2. 각 banned_id에 해당하는 아이디로 조합을 만든 후 조합의 개수 구하기
# 3. banned_id 인지 확인
# 1) 글자 수 비교
# 2) 각 자리의 글자를 하나씩 가져오면서 확인(zip)
# 3) 이 때, * 글자의 경우에는 그냥 넘어가기
# permutation으로 user_id에서 가능한 순서들을 먼저 구한 후 비교!

from itertools import permutations
from collections import defaultdict

def solution(user_id, banned_id):
    answer = []
    banned_dict = defaultdict(set)
    for ban in banned_id:
        for user in user_id:
            if len(ban) == len(user):
                banned = True
                for b_s,u_s in zip(ban,user):
                    if b_s != '*' and b_s != u_s:
                        banned = False
                        break
                if banned == True:
                    banned_dict[ban].add(user)
    banned_list = []
    for i in banned_id:
        banned_list.append(list(banned_dict[i]))

    for j in permutations(user_id, len(banned_id)):
        cnt = 0
        for a,b in zip(j,banned_id):
            if a in banned_dict[b]:
                cnt += 1
        if cnt == len(banned_id):
            j = sorted(set(j))
            if j not in answer:
                answer.append(j)
    #print(answer)
    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["*rodo", "*rodo", "******"]

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id, banned_id))
