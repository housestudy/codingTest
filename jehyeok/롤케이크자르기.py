topping = [1, 2, 1, 3, 1, 4, 1, 2]

# def solution(topping):
#     answer = 0

#     for i in range(1, len(topping)):
#         chulsoo = set(topping[0:i])
#         brother = set(topping[i:len(topping)])

#         if len(chulsoo) == len(brother):
#             answer += 1

#     return answer

# print(solution(topping))

# 답
# 파이썬에서 Dict을 써본적이 없다... Counter 함수도 처음봤다... 에휴...
from collections import Counter

def solution(topping):
    answer = 0

    # 이렇게 만들면 각 value값이 key로 들어가고
    # 해당 value의 개수가 value값이 된다.
    # 예를 들어 topping = [1, 2, 3, 1, 4]면 Counter({1: 2, 2: 1, 3: 1, 4: 1}) 이렇게 된다.

    # 우선은 철수가 모든 토핑을 가져가고 동생은 아무것도 가져가지 않은 상태로 초기화
    chulsoo = Counter(topping)
    brother = set()

    # 철수가 가진 토핑을 동생에게 하나씩 주면서, 서로 가진 토핑의 개수가 일치하면 answer += 1
    for i in topping:
        chulsoo[i] -= 1
        brother.add(i)

        # 특정 토핑이 없다면 해당 토핑을 지워준다.
        # 그렇지 않으면 len 비교할 때 없는 토핑도 비교되니까.. 즉, 철수한테 그 토핑이 없는데 개수 셀 때는 포함되어버림
        if chulsoo[i] == 0:
            chulsoo.pop(i)
        if len(chulsoo) == len(brother):
            answer += 1
    
    return answer

print(solution(topping))