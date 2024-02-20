# 내 정답
# 정답 코드를 보니... 굳이 1~M개를 선택하지 말고 M개에 대한 조합만 생각해도 된다...
from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().strip().split())

maps = []

for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().strip().split())))

chickens = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            chickens.append((i, j))

min_distance = 1e9

for chicken in list(combinations(chickens, M)): # 치킨집 i개를 선택하는 모든 조합에 대해
    distance = 0
    
    for j in range(N):
        for k in range(N):
            if maps[j][k] == 1: # 각각 집에서
                min_dis = abs(j - chicken[0][0]) + abs(k - chicken[0][1]) # 치킨 조합의 첫 번째 치킨집 까지의 거리가 최소라고 해놓고
                for data in chicken: # 치킨 조합의 모든 치킨집에 대해 집에서 치킨집 까지의 최소 거리를 구하고
                    tmp_dis = abs(j - data[0]) + abs(k - data[1])
                    if tmp_dis < min_dis:
                        min_dis = tmp_dis

                distance += min_dis # 최소 거리를 구해 거리에 더해준다.

    if distance < min_distance:
        min_distance = distance

print(min_distance)