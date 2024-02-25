from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    left_max = len(queue1)
    right_max = len(queue2)
    cnt = 0
    left = 0
    right = 0
    sum1 = sum(q1)
    sum2 = sum(q2)
    while True:
        if sum1 < sum2:
            tmplf = q2.popleft()
            q1.append(tmplf)
            left += 1
            sum2 -= tmplf
            sum1 += tmplf
        elif sum1 > sum2 :
            tmprt = q1.popleft()
            q2.append(tmprt)
            right += 1
            sum1 -= tmprt
            sum2 += tmprt
        else:
            return left + right
        cnt = left + right
        if cnt > 2*(left_max + right_max)+1:
            return -1
