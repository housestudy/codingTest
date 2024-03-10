from collections import deque

queue1 = [1, 1]
queue2 = [1]

def solution(queue1, queue2):
    answer = 0

    # 총 합이 홀수면 두 큐를 같게 만들 수 없음
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    queue1Sum = sum(queue1)
    queue2Sum = sum(queue2)

    while True:
        if len(queue1) == 0 or len(queue2) == 0:
            answer = -1
            break

        # queue1 과 queue2가 서로 뒤바뀌었을때
        if 2 * (len(queue1) + len(queue2)) < answer:
            answer = -1
            break

        if queue1Sum == queue2Sum:
            break

        if queue1Sum > queue2Sum:
            v = queue1.popleft()
            queue2.append(v)
            queue1Sum -= v
            queue2Sum += v
        else:
            v = queue2.popleft()
            queue1.append(v)
            queue2Sum -= v
            queue1Sum += v

        answer += 1

    return answer

print(solution(queue1, queue2))