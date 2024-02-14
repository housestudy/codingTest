import itertools

def solution(relations):
    answer = 0
    rows = len(relations)
    cols = len(relations[0])
    keys = [[] for _ in range(cols)]
    answers = []
    candies = []
    for i in range(1,cols+1):
        candies.append(list(itertools.combinations(range(cols),i)))

    # 유일성검사
    def ck_duplicate(seq):
        seen = []
        unique_list = [x for x in seq if x not in seen and not seen.append(x)]
        return len(seq) == len(unique_list)

    # 조합된 key 만들기
    def combi(arr):
        combined_keys = []
        for i in range(rows):
            temp = []
            for j in arr:
                temp.append(keys[j][i])    
            combined_keys.append(temp)
        return combined_keys

    # 분리해서 key별로 정리
    for relation in relations:
        for i in range(cols):
            keys[i].append(relation[i])

    for candi in candies:
        for x in candi:
            combined_keys = combi(x)
            ck_result = ck_duplicate(combined_keys)
            if ck_result:
                temp = ''.join(map(str,x))
                answers.append(list(temp))

    # minimal 체크
    def ck_minimal(std, target):
        flag = len(std)
        for s in std:
            for t in target:
                if s == t :
                    flag -= 1
                if flag == 0:
                    return False
        return True

    ans_len = len(answers)
    flag = [True for _ in range(ans_len)]
    for i in range(ans_len):
        for j in range(i+1, ans_len):
            if flag[j] :
                # if answers[i] in answers[j]:
                    # flag[j] = False
                # 이 부분에서 단순 str 처리하는 것으로 테케 몇개가 통과가 안됐다. 왜냐면 03은 013을 제거하지 못하기 때문.
                min_ckeck = ck_minimal(answers[i], answers[j])
                if min_ckeck == False:
                    flag[j] = False

    for f in flag:
        if f : answer += 1

    return answer