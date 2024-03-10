# 의상의 종류별로 dict 형태로 정리
# 의상의 종류의 개수 + 1(안입을 경우)
# 마지막에 전체 경우에서 모두 안 입는 경우를 빼주기

from collections import defaultdict

tc = int(input())
for _ in range(tc):
    result = 1
    n = int(input())
    clothes_dict = defaultdict(list)
    for i in range(n):
        clothes, clothes_type = input().split()
        clothes_dict[clothes_type].append(clothes)

    for cloth in clothes_dict:
        result *= len(clothes_dict[cloth])+1

    print(result-1)