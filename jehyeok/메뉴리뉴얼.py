orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]

from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        maxCnt = 0
        result = []

        for order in orders:
            for data in combinations(order, c):
                tmp = list(data)
                cnt = 0
                for o in orders:
                    test = [x for x in o if x in tmp]

                    if len(test) == c: cnt += 1

                if cnt <= 1:
                    continue
                if cnt == maxCnt:
                    tmp.sort()
                    result.append(''.join(tmp))
                elif cnt > maxCnt:
                    tmp.sort()
                    result = [''.join(tmp)]
                    maxCnt = cnt

        for data in list(set(result)):
            answer.append(data)

    answer.sort()

    return answer

print(solution(orders, course))