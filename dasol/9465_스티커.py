import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    stickers = []
    length = int(input())
    for i in range(2):
        stickers.append(list(map(int, input().split())))
    
    dp = [[0 for _ in range(2)] for _ in range(length)]
    # dp 없이 기본 입력 그래프만으로도 풀 수 있기는 함

    dp[0][0] , dp[0][1] = stickers[0][0], stickers[1][0]
    if length > 1:
        dp[1][0] , dp[1][1] = stickers[0][1] + dp[0][1], stickers[1][1] + dp[0][0]

    for i in range(2,length):
        dp[i][0] = max(dp[i-1][1] + stickers[0][i], max(dp[i-2]) + stickers[0][i])
        dp[i][1] = max(dp[i-1][0] + stickers[1][i], max(dp[i-2]) + stickers[1][i])

    print(max(dp[length-1]))