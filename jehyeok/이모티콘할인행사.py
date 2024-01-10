# https://school.programmers.co.kr/learn/courses/30/lessons/150368
# Lv2. 2023 카카오

# 내 생각
# 중복순열 문제인듯? 이모티콘이랑 유저 최대 수가 많지 않아서..
# 이모티콘들의 모든 할인된 가격을 저장해서
# 예를 들면 전부 40% 할인된거나, 40/40/40/30 할인된거나
# 싹다 저장해서
# 각 유저마다 계산

from itertools import product

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]

def solution(users, emoticons):
    answer = []
    plusUser = 0
    total = 0

    rates = [10, 20, 30, 40]

    calculatedEmoticons = []
    for rate in product(rates, repeat=len(emoticons)):
        tmp = [(rate[i], emoticons[i] * (100 - rate[i]) * 0.01) for i in range(len(emoticons))]
        calculatedEmoticons.append(tmp)

    result = []

    for data in calculatedEmoticons:
        plusUser = 0
        total = 0

        for rate, maximum in users: # O(100)
            sumData = sum([x[1] for x in data if x[0] >= rate]) # O(7)
            if sumData >= maximum:
                plusUser += 1
            else:
                total += sumData

        result.append([plusUser, total])

    result = sorted(result, key=lambda x: (x[0], x[1]), reverse=True)

    answer = result[0]
    return answer

print(solution(users, emoticons))

# 100점~ 34분 컷!