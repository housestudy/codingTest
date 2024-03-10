# 조건
# 1. 2가지 이상의 단품메뉴로 구성
# 2. 2명 이상의 손님으로부터 주문된 단품 메뉴들
# 풀이1
# 1. 각 손님별로 주문한 단품 메뉴를 리스트로 저장
# 2. 추가하고 싶어하는 코스요리의 단품 메뉴 개수 별로 가능한 조합들 구하기
# 3. 손님들을 완전탐색하면서 그 조합의 단품 메뉴들이 있는지 확인
# 4. 3번에서 탐색하면서 주문된 조합들을 dict로 저장
# => 4,5중 for문
# 풀이2
# 1. 각 손님별로 course 개수 별 가능한 조합 구해
# 2. 구한 걸로 dict에 저장
# 3. 해당 dict에서 value의 값이 2이상인 경우 answer에 저장

from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        course_dict = defaultdict(int)
        for order in orders:
            com = list(combinations(sorted(order),c))
            for combin in com:
                course_dict[''.join(combin)] += 1
        course_sort = sorted(course_dict.items(), key = lambda x:-x[1])
        max = 0
        for menu, num in course_sort:
            if num < 2:
                break
            if num >= max:
                answer.append(menu)
                max = num
            else:
                break
    answer.sort()
    return answer

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))
