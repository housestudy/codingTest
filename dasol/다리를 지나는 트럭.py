from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    cur_weight = 0
    idx = 0
    answer = 0
    while idx < len(truck_weights):
        if cur_weight + truck_weights[idx] <= weight :
            cur_weight += truck_weights[idx]
            bridge[-1] = truck_weights[idx]
            idx += 1
        front = bridge.popleft()
        bridge.append(0)
        answer += 1
        if front != 0 :
            cur_weight -= front
    while bridge :
        bridge.popleft()
        answer += 1        
    return answer