# n : 배달할 집의 개수
# cap : 트럭에 담을 수 있는 택배 상자 최대 개수
# deliveries : 각 집에 배달할 재활용 택배 상자의 개수
# pickups : 각 집에서 수거할 빈 재활용 택배 상자 개수
# 최소 이동 거리 구하기
# 배달할 택배 또는 수거할 택배가 있는 집이 있을 때 해당 집으로 이동 해야함

def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    delivery_cnt = 0
    pickup_cnt = 0

    for house in range(n):
        delivery_cnt += deliveries[house]
        pickup_cnt += pickups[house]

        while delivery_cnt > 0 or pickup_cnt > 0:
            delivery_cnt -= cap
            pickup_cnt -= cap
            answer += (n-house)*2
    return answer


cap = 4
n = 5
deliveries = [1,0,3,1,2]
pickups = [0,3,0,4,0]
print(solution(cap,n,deliveries,pickups))