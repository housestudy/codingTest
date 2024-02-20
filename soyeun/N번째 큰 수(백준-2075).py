# 1. 각 행 별로 정렬
# 2. 아래 행으로 갈수록 큰 수
# 3. 아래 행부터 확인
# 4. deque 활용
# 5. 최소힙 활용

import sys
import heapq

input = sys.stdin.readline
n = int(input())

queue = []

for _ in range(n):
    input_num = list(map(int,input().split()))
    if not queue:
        for num in input_num:
            heapq.heappush(queue, num)
    else:
        for num in input_num:
            if queue[0] < num:
                heapq.heappop(queue)
                heapq.heappush(queue,num)
print(queue[0])

