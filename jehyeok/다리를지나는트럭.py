from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# bridge_length + truck_weights + group 개수
# 에다가 group 사이의 간격까지 하면 될듯?
# onBridge에 0을 넣어가면서 0의 개수가 전체 간격 아닐까?
def solution(bridge_length, weight, truck_weights):
    answer = 0

    truck_weights = deque(truck_weights)
    onBridge = deque([]) # 다리 위에 있는 트럭
    currentTime = 0 # 맨 앞 트럭이 다리를 통과하고 있는 시간
    gap = 0 # 맨 앞 트럭과 맨 트럭의 시간 간격

    while len(truck_weights) != 0:
        # 시간 흐르고
        answer += 1
        if len(onBridge) != 0: currentTime += 1

        # 맨 앞 차가 다리를 통과했을때
        if currentTime > bridge_length:
            onBridge.popleft()
            currentTime -= gap

        # 이제 지나갈 트럭이 없으면
        if len(truck_weights) == 0:
            break

        # 다리에 올라갈 수 있는지 확인하고
        # 다리에 올라갈 수 없으면 continue
        if sum(onBridge) > weight:
            gap += 1
            continue

        # 다리에 올라갈 수 있으면 다리에 올림
        else:
            onBridge.append(truck_weights.popleft())

    return answer

print(solution(bridge_length, weight, truck_weights))

# 답
# 어렵게 생각할 이유도 없었고~ 수학적인 사고는 뭔 쓰잘데기 없는 짓이냐~
def solution(bridge_length, weight, truck_weights):
    
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    currentWeight = 0
    while len(truck_weights) != 0:
        time += 1

        currentWeight -= bridge.popleft()

        if currentWeight + truck_weights[0] <= weight:
            currentWeight += truck_weights[0]
            bridge.append(truck_weights.popleft())

        else: 
            bridge.append(0)
            
    time += bridge_length
    
    return time
