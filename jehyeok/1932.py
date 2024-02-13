import sys

n = int(sys.stdin.readline())
dp = []

for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1, n):
    for j in range(0, i + 1):
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]

        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]

        dp[i][j] = dp[i][j] + max(up, up_left)

print(max(dp[n - 1]))