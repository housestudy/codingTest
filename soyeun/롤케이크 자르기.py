# 철수와 동생이 먹을 수 있는 토핑의 종류와 개수에 대해 딕트로 저장
from collections import Counter, defaultdict
def solution(topping):
    answer = 0
    A_dict = defaultdict(int)
    B_dict = Counter(topping)

    for i in topping:
        A_dict[i] += 1
        B_dict[i] -= 1
        if B_dict[i] == 0:
            del B_dict[i]
        if len(A_dict) == len(B_dict):
            answer += 1
        if len(A_dict) > len(B_dict):
            break

    return answer

topping = [1, 2, 3, 1, 4]
print(solution(topping))