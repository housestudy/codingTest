# https://school.programmers.co.kr/learn/courses/30/lessons/169198
# Lv 2.

# 내 답
# 일단 80.6점이고...
# 수학적으로 튕긴다는건 (x, y)를 특정 축에 대해 대칭 이동 시켜 (startX, startY)와 대칭 이동 된 점까지의 거리를 구하면 된다.
# 이 상태에서 고려해야될게 x == 0 or y == 0일 때와, startX == x or startY == y 일때라 생각했고
# 그에 대한 예외처리를 했으나... x, y를 문제에서 실제 수학에서와 동일하게 했을줄은 몰랐다.
# 당연히 y축이 x고, x축이 y일 줄 알았지... 프로그래밍 문제인데 수학이랑 동일하게 해놓을줄은...
# 다행히 정답 테스트에서 테스트 29번까지는 예외 처리 없이 대칭 이동만 시키면 맞는 문제 같다.
m, n, startX, startY = 10, 10, 3, 7
balls = [[7, 7], [2, 7], [7, 3]]

def solution(m, n, startX, startY, balls):
    answer = []

    for ball in balls:
        x, y = ball[0], ball[1]

        # 상하좌우
        tmpx1, tmpx2, tmpx3, tmpx4 = -x, m + (m - x), x, x
        tmpy1, tmpy2, tmpy3, tmpy4 = y, y, -y, n + (n - y)

        result1 = abs(startX - tmpx1) * abs(startX - tmpx1) + abs(startY - tmpy1) * abs(startY - tmpy1)
        result2 = abs(startX - tmpx2) * abs(startX - tmpx2) + abs(startY - tmpy2) * abs(startY - tmpy2)
        result3 = abs(startX - tmpx3) * abs(startX - tmpx3) + abs(startY - tmpy3) * abs(startY - tmpy3)
        result4 = abs(startX - tmpx4) * abs(startX - tmpx4) + abs(startY - tmpy4) * abs(startY - tmpy4)

        if startX == 0:
            result1 = 1000000

        if startY == 0:
            result3 == 1000000
        
        if x == startX:
            if y > startY:
                result4 = 1000000
            else:
                result3 = 1000000

        if y == startY:
            if x > startX:
                result1 = 1000000
            else:
                result2 = 1000000
            

        answer.append(min(result1, result2, result3, result4))

    return answer

print(solution(m, n, startX, startY, balls))

# 정답
def solution(m, n, startX, startY, balls):
    answer = []
    start = [startX,startY]
    for i in range(len(balls)):
        end = [balls[i][0], balls[i][1]]
        distance = 10**10
        temp = []
        if start[0]!=end[0] or start[1] > end[1]: 
            temp.append(abs(start[0]-end[0])**2 + abs(2*n-start[1]-end[1])**2)  #우
        if start[0]!=end[0] or start[1] < end[1]: 
            temp.append(abs(start[0]-end[0])**2 + abs(start[1]+end[1])**2)      #좌
        if start[1]!=end[1] or start[0] < end[0]: 
            temp.append(abs(start[0]+end[0])**2 + abs(start[1]-end[1])**2)      #상
        if start[1]!=end[1] or start[0] > end[0]: 
            temp.append(abs(2*m-start[0]-end[0])**2 + abs(start[1]-end[1])**2)  #하
        for dist in temp:
            if dist < distance:
                distance = dist
        answer.append(distance)
    return answer