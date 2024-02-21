# 그리디 문제 같음
# 1. 두 큐의 총합을 구하여 같게 만들어주기 위한 값을 알아냄
# 2. 각 큐의 총합을 보면서 1번에서 알아낸 값보다 작다면 다른 큐에서 pop하여 가져오기
# 3. 종료 시점 : queue1과 queue2의 총 개수만큼 했을 때도 답이 안나오면 멈추기

from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    limit = len(queue1)*4


    if (queue1_sum + queue2_sum)%2 != 0:
        return -1

    while True:
        if queue1_sum < queue2_sum:
            num = queue2.popleft()
            queue1.append(num)
            queue1_sum += num
            queue2_sum -= num
            answer += 1

        elif queue1_sum > queue2_sum:
            num = queue1.popleft()
            queue2.append(num)
            queue1_sum -= num
            queue2_sum += num
            answer += 1

        else:
            break

        if answer == limit:
            return -1
    return answer

# queue1 = [3, 2, 7, 2]
# queue2 = [4,6,5,1]
queue1 = [1,1]
queue2 = [1,5]
print(solution(queue1, queue2))