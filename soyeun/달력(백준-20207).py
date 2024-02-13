# 1. 주어진 시작 날짜와 종료 날짜 리스트를 시작 날짜를 기준으로 정렬
# 2. 시작 날짜의 index와 종료 날짜의 index를 이용하여 가로 길이 구하기
# 3. 2번에서 계산 시 해당 index 안에 포함될 때 세로 길이를 하나씩 더하기(height 리스트 활용)
# => 스케줄을 정리한 리스트를 이용하여 구하기
n = int(input())
result = 0
schedule = [0]*366

for _ in range(n):
    s,e = map(int, input().split())
    for i in range(s, e+1):
        schedule[i] += 1

col = 0
row = 0
for day in schedule:
    if day == 0:
        result += col * row
        col = 0
        row = 0
    else:
        col = max(col, day)
        row += 1
result += col*row
print(result)
