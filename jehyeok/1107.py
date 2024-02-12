# ...? 아예 못풀겠는데요...
# 일단 뭔가 로직을 써서 풀려고 한 순간 나가리인 문제였고..
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

breakedNums = list(map(int, input().strip().split()))
btns = [x for x in range(10) if x not in breakedNums]

nums = []
for i in str(N):
    nums.append(int(i))

current = 100
cnt = 0

for num in nums:
    for i in range(10):
        if i in breakedNums:
            continue


# 정답
N = int(input())
M = int(input())

breakedNums = list(map(int, input().strip().split()))
btns = [str(x) for x in range(10) if x not in breakedNums]

min_cnt = abs(100 - N) # 일단 100과의 갭을 최소로 두고 계산

# 채널 번호는 50만까지밖에 없지만
# 100만 근처까지 갔다가 -1씩 해서 돌아오는 케이스까지 있을 수 있으니 range = 100만
# 즉, 이 문제는 1~999999까지 모든 숫자를 돌면서
# 해당 숫자부터 N까지 갈 때 필요한 버튼의 수의 최소값을 갱신시키는 문제
# 어차피 해봤자 O(100만 * 6) 밖에 안된다.
for k in range(1000000):
    num = str(k)

    for i in range(len(num)):
        # num의 각 자리 수 중에 누를 수 없는 수에 해당하는게 하나라도 있는 숫자면 제외..
        # 여기가 이해가 안 갔는데..
        # 예제 1. 5457 이라고 생각했을때
        # 어차피 i = 5455인 케이스에 대해서 min_cnt를 넣어줬기 때문에
        # 5456, 5457과 같은 숫자는 제외해도 상관없구나
        if num[i] not in btns:
            break
        # 마지막자리까지 모두 누를 수 있는 수면
        if i == len(num) - 1:
            # min(기존 답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
            min_cnt = min(min_cnt, len(num) + abs(N - k))

print(min_cnt)