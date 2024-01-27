# https://school.programmers.co.kr/learn/courses/30/lessons/148653
# Lv 2. 

# 내 답
# ..? 테스트케이스 꼬라지 보니 remain이 0일때 아니면 5일때에 대한 예외케이스일텐데
# 둘다 모르겠는데?
# 공책좀 가져올걸 ㅎ
storey = 9488

def solution(storey):
    answer = 0

    while storey > 0:
        remain = storey % 10
        
        if remain < 5:
            answer += remain
            storey = storey // 10
        elif remain == 5:
            if (storey // 10) % 10 > 4:
                answer += 10 - remain
                storey = storey // 10 + 1
            else:
                answer += remain
                storey = storey // 10
        else:
            answer += 10 - remain
            storey = storey // 10 + 1

    return answer

print(solution(storey))