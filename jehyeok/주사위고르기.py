dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]

from itertools import combinations
from itertools import product
from bisect import bisect_left

def solution(dice):
    answer = []

    N = len(dice)
    # dice에서 한개 고르면 배열이 나와서 복잡하니까 몇번째 주사위를 고르는지 index로 체크하려고
    diceIdx = [x for x in range(N)]

    # 전체 주사위 오름차순 정렬
    tmpDice = []
    for i in dice:
        i.sort()
        tmpDice.append(i)
    dice = tmpDice

    # 최대승수
    maxWinCnt = 0

    # 주사위를 고르는 모든 경우의 수
    for myDice in combinations(diceIdx, N // 2):
        # [1, 2], [1, 4] 이런 느낌
        myDice = list(myDice)
        yourDice = [x for x in diceIdx if x not in myDice]

        winCnt = 0

        mySums = []
        yourSums = []

        # 모든 합들
        for i in product([0, 1, 2, 3, 4, 5], repeat=(N // 2)):
            mysum = 0
            yoursum = 0
            for j in range(N // 2):
                mysum += dice[myDice[j]][i[j]]
                yoursum += dice[yourDice[j]][i[j]]
            mySums.append(mysum)
            yourSums.append(yoursum)

        yourSums.sort()

        for sum in mySums:
            winCnt += bisect_left(yourSums, sum)
        
        if maxWinCnt < winCnt:
            answer = myDice
            maxWinCnt = winCnt

    result = []
    for x in answer:
        result.append(x + 1)
    
    return result

print(solution(dice))