# 자기보다 큰 사람이 왼쪽에 몇 명 있었는지 기억
# 자신보다 큰 사람의 수를 하나씩 가져오면서 result 리스트의 해당 index에 배정되어있지 않고 키 큰 사람의 수가 같으면 배정
# 키 큰 사람의 수가 같지 않지만 해당 자리가 0인 경우 카운트

n = int(input())
cnt_list = list(map(int,input().split()))
result = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if result[j] == 0 and cnt_list[i] == cnt:
            result[j] = i+1
            break
        elif result[j] == 0:
            cnt += 1
print(*result)
