import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        # 역시 파이썬이면 이렇게 쓸 수 있을 줄 알았다
        heapq.heappush(heap, (abs(x), x))