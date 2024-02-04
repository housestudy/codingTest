# DPDPDPDPDPDPDP
import sys

N = int(sys.stdin.readline())

cost = []
for i in range(N):
    cost.append(list(map(int, sys.stdin.readline().strip().split())))

dp = [[0] * 3 for _ in range(N)]
dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1] + cost[i][0], dp[i - 1][2] + cost[i][0])
    dp[i][1] = min(dp[i - 1][0] + cost[i][1], dp[i - 1][2] + cost[i][1])    
    dp[i][2] = min(dp[i - 1][0] + cost[i][2], dp[i - 1][1] + cost[i][2])

print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))