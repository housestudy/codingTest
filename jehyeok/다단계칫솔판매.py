enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

# ...이걸 어떻게 O(nlogn) 안쪽으로 풀지..?
import math

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)

    enrollDict = {}

    for idx, person in enumerate(enroll):
        enrollDict[person] = idx

    for idx, person in enumerate(seller):
        findIdx = enrollDict[person]
        money = amount[idx] * 100

        while True:
            notMyMoney = math.trunc(money * 0.1)
                        
            myMoney = money - notMyMoney
            # 본인 돈부터 넣고
            answer[findIdx] += myMoney
            # 추천인 찾아서
            refer = referral[findIdx]

            if refer == '-':
                break

            # 이게 신의 한수네... amount가 해봤자 10000원인데
            # 그럼 최대 4번밖에 안가네
            if notMyMoney < 1: break

            findIdx = enrollDict[refer]
            money = notMyMoney

    return answer

print(solution(enroll, referral, seller, amount))