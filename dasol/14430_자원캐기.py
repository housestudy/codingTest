import sys
# 입력
input = sys.stdin.readline
N, M = map(int, input().split())
resources = []
for i in range(N):
    resources.append(list(map(int, input().split())))

result=[[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i==0 and j==0:
            result[i][j]=resources[i][j]
        elif i==0 and j!=0:
            result[i][j]=resources[i][j]+result[i][j-1]
        elif i!=0 and j==0:
            result[i][j]=resources[i][j]+result[i-1][j]
        else:
            result[i][j]=resources[i][j]+max(result[i-1][j],result[i][j-1])
print(result[N-1][M-1])