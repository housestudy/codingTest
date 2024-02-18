import sys
input = sys.stdin.readline

# T = int(input())

def calculateDistance(a, b, c):
    answer = 0

    for i in range(4):
        if a[i] != b[i]:
            answer += 1
        if c[i] != b[i]:
            answer += 1
        if c[i] != a[i]:
            answer += 1

    return answer

# 1안
# for _ in range(T):
#     N = int(input())
#     arr = list(map(str, input().strip().split()))
    
#     minDistance = 0

#     a, b, c = arr[0], arr[1], arr[2]
#     minDistance = calculateDistance(a, b, c)
#     # 이렇게 하면 답이 없어 보이고... 걍 combinations 돌리는거랑 뭐가 달라
#     for i in range(3, N):
#         break


# 2안
# ㅋㅋ 이건 그냥 지금 예제만 가지고 하는거고
# for _ in range(T):
#     N = int(input())
#     arr = list(map(str, input().strip().split()))
    
#     arr = sorted(arr, reverse=True)
#     Iarr = [x for x in arr if x[0] == 'I']
#     Earr = [x for x in arr if x[0] == 'E']

#     # I 3개
#     a, b, c = Iarr[0], Iarr[1], Iarr[2]
#     answer0 = calculateDistance(a, b, c)

#     # I 2개, E 1개
#     a, b, c = Iarr[0], Iarr[1], Earr[0]
#     answer1 = calculateDistance(a, b, c)

#     # I 1개, E 2개
#     a, b, c = Iarr[0], Earr[0], Earr[1]
#     answer2 = calculateDistance(a, b, c)

#     # E 3개
#     a, b, c = Earr[0], Earr[1], Earr[2]
#     answer3 = calculateDistance(a, b, c)

#     print(min(answer0, answer1, answer2, answer3))


# 3안
# 어차피 결국 MBTI는 16개밖에 없는거 아닌가
# 그럼 set으로 중복 다 없애고 그 중에 3개 조합하는건?
# 이렇게 하니까 또 MBTI 겹칠때가 힘드네...

from itertools import combinations

# for _ in range(T):
#     result = 0

#     N = int(input())
#     arr = list(set(list(map(str, input().strip().split()))))
    
#     if len(arr) == 1:
#         result = 0
#         break

    
# 4안
# ㅋㅋ 그럼 dict로? 라고 생각해봤지만 이건 결국 개수가 들어가니 완전탐색 combinations랑 똑같겠고만...
# from collections import Counter

# for _ in range(T):
#     N = int(input())
#     arr = Counter(list(map(str, input().strip().split())))
    
#     if len(arr) == 1:
#         print(0)
#         break

# 답...
# 뭔 비둘기집 원리라는데...
# 비둘기집 원리 : N + 1개의 물건을 N 개의 상자에 넣은 경우, 최소한 한 상자에는 그 물건이 반드시 2개 이상 들어있다는 원리

# 즉, 여기서는 MBTI 종류가 최대 16개 이고, 3명을 선택해야 되기 때문에 N이 33개를 넘기면 무조건 답이 0이라는 뜻
# 그렇기 때문에 N이 33을 넘으면 0 출력하고, 아니면 combinations를 쓴다...
# 천잰데..?
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(str, input().strip().split()))

    if N > 32:
        print(0)
        continue
    
    minDistance = 1e9

    for data in combinations(arr, 3):
        a, b, c = data[0], data[1], data[2]
        minDistance = min(calculateDistance(a, b, c), minDistance)

    print(minDistance)