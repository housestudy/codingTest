# 행 별로 가져오면서 1과 1사이에 0의 개수를 세기
# 0의 개수를 셀 때, 1을 기준으로 split 해주기

h, w = map(int, input().split())
wall_list = list(map(int, input().split()))
graph = [['0']*w for _ in range(h)]
result = 0

for column in range(w):
    for row in range(h-wall_list[column],h):
        graph[row][column] = '1'

for wall in graph:
    rain_list = ''.join(wall).split('1')
    n = len(rain_list)
    if n >= 3:
        for i in range(1,n-1):
            result += len(rain_list[i])
print(result)
# for wall in graph:
#     start = False
#     cnt = 0
#     for w in wall:
#         if w == 1 and start == False:
#             start = True
#         elif w == 1 and start == True:
#             if cnt != 0:
#                 start = False
#                 result += cnt
#                 cnt = 0
#         elif w == 0 and start == True:
#             cnt += 1

