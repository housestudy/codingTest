n = int(input())
input_list = [list(map(int, input().split())) for _ in range(n)]
input_list = sorted(input_list)
max_height = 0
max_idx = 0
result = 0

for i in range(n):
    if input_list[i][1] > max_height:
        max_height = input_list[i][1]
        max_idx = i

height = input_list[0][1]

# 기둥의 길이가 가장 긴 것의 왼쪽 부분
for j in range(max_idx):
    if input_list[j+1][1] > height:
        result += (input_list[j+1][0]-input_list[j][0])*height
        height = input_list[j+1][1]
    else:
        result += (input_list[j + 1][0] - input_list[j][0]) * height

height = input_list[-1][1]

for j in range(n-1, max_idx,-1):
    if input_list[j-1][1] > height:
        result += (input_list[j][0]-input_list[j-1][0])*height
        height = input_list[j-1][1]
    else:
        result += (input_list[j][0]-input_list[j-1][0])*height

print(result + max_height)

# 이건 뭐가 문제인지 모르겠음....

# 1. 오목하게 들어간 부분이 없어야 함
# 2. 일단 각 기둥의 왼쪽 면의 위치를 기준으로 정렬
# 3. 차례대로 기둥의 높이를 가져옴
# 4. 다음 기둥의 높이가 현재보다 클 경우 면적 계산 => (다음 시작 위치 - 현재 시작 위치)*(두 기둥의 높이 차)
# 5. 다음 기둥의 높이가 현재보다 작을 경우 패스
# 6. 5번에서 마지막 기둥인데 현재보다 작을 경우 현재 기둥과 마지막 기둥으로 4번 계산 진행

# from collections import deque
#
# n = int(input())
# input_list = [list(map(int, input().split())) for _ in range(n)]
# input_list = sorted(input_list)
# input_list = deque(input_list)
# answer = 0
# pre_l, pre_h = input_list.popleft()
#
# while input_list:
#     next_l, next_h = input_list.popleft()
#     if pre_h <= next_h:
#         answer += (next_l-pre_l)*pre_h
#         pre_l, pre_h = next_l, next_h
#
#         if len(input_list) == 0:
#             answer += next_h
#     else:
#         if len(input_list) == 0:
#             answer += (next_l+1-pre_l)*next_h
#             answer += (pre_h - next_h)
#
# print(answer)
