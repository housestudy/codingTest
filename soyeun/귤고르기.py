# 1. 귤의 종류별 개수를 dict로 만들기
# 2. 해당 dict를 개수를 기준으로 내림차순 정렬
# 3. 하나씩 빼오면서 개수의 합이 k보다 크거나 같으면 stop, 귤 종류의 개수 세기

from collections import Counter

def solution(k, tangerine):
    answer = 0
    tangerine_dict = Counter(tangerine)
    tang_list = sorted(tangerine_dict.items(),key=lambda x:-x[1])

    for tang_type, cnt in tang_list:
        answer += 1
        k -= cnt
        if k <= 0:
            break
    return answer

k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k,tangerine))