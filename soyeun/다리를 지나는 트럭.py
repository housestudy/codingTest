# 1. 트럭이 다리를 올라가면 bridge_length 시간 만큼 머물러야 하네
# 2. queue 활용?
# 4. bridge라는 queue 생성
# 5. 대기 트럭을 하나씩 가져와서 bridge에 올려
# 6. 만약 weight보다 작으면 하나 더 올려
# 7. 현재 bridge의 무게와 대기 트럭의 첫번째 트럭과 합한 무게가 weight보다 클 경우 0 추가

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    bridge_weight = 0
    truck_weights = deque(truck_weights)

    while truck_weights:
        if len(bridge) == bridge_length:
            num = bridge.popleft()
            bridge_weight -= num
        if bridge_weight + truck_weights[0] <= weight:
            num = truck_weights.popleft()
            bridge.append(num)
            bridge_weight += num
        elif bridge_weight + truck_weights[0] > weight:
            bridge.append(0)

        answer += 1

    return answer + bridge_length

# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

print(solution(bridge_length, weight, truck_weights))
