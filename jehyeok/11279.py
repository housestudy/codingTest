# 기본적으로 파이썬의 heap은 최소힙이다.
# 최대힙은 지원하지 않기 때문에
import heapq
import sys

heap = []

N = int(input())

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            # 2. 출력할 때 다시 -를 붙여 출력한다.
            print(-heapq.heappop(heap))
    else:
        # 1. 데이터를 넣을 때는 -를 붙어 집어넣고
        heapq.heappush(heap, -x)

# 그리고 이 문제 풀면서 느낀건
# 다시 sys.stdin으로 입력을 받아야겠다...
# 이거 그냥 input()으로 하면 시간초과 뜬다