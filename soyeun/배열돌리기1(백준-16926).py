
# 1차원으로 만든 후 회전
from collections import deque

n, m, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
result = [[0]*m for _ in range(n)]

cnt = min(n,m)//2
for i in range(cnt):
    queue = deque()
    queue.extend(array[i][i:m-i])
    queue.extend([row[m-i-1] for row in array[i+1:n-i-1]])
    queue.extend(array[n-i-1][i:m-i][::-1])
    queue.extend([row[i] for row in array[i+1:n-i-1][::-1]])
    #print('queue:',queue)
    queue.rotate(-r)
    #print('queue:', queue)

    for j in range(i,m-i):
        result[i][j] = queue.popleft()
    for j in range(i+1,n-i-1):
        result[j][m-i-1] = queue.popleft()
    for j in range(m-i-1,i-1,-1):
        result[n-i-1][j] = queue.popleft()
    for j in range(n-i-2,i,-1):
        result[j][i] = queue.popleft()

for line in result:
    print(*line)


# 행을 기준으로 생각하기
# [첫 행, 마지막행],[두번째 행, 끝에서 두번째 행]
# for 문을 이용하여 행끼리 짝 만들기
# A[1][1] ← A[1][2] ← A[1][3] ← A[1][4] ← A[1][5]
#    ↓                                       ↑
# A[2][1]   A[2][2] ← A[2][3] ← A[2][4]   A[2][5]
#    ↓         ↓                   ↑         ↑
# A[3][1]   A[3][2] → A[3][3] → A[3][4]   A[3][5]
#    ↓                                       ↑
# A[4][1] → A[4][2] → A[4][3] → A[4][4] → A[4][5]
from copy import deepcopy

# n, m, r = map(int, input().split())
# array = [list(map(int, input().split())) for _ in range(n)]
#
# for _ in range(r):
#     temp_array = [[0]*m for i in range(n)]
#     for row in range(n//2):
#         for column in range(m):
#             if column == row:
#                 temp_array[row+1][column] = array[row][column]
#                 temp_array[n-row-1][column+1] = array[n-row-1][column]
#             elif column == m-row-1:
#                 temp_array[row-1][column-1] = array[row][column-1]
#                 temp_array[row][column-1] = array[row][column]
#             else:
#                 print('row, column',row,column)
#                 temp_array[row][column] = array[row][column+1]
#                 temp_array[n-row-1][column] = array[row][column]
#     array = temp_array
#     print(array)

