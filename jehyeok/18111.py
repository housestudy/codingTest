# https://www.acmicpc.net/problem/18111
# 실버2
# ... 틀렸다는데 예제가 다 맞았잖아 하... 제발 틀린 케이스도 좀 알려줬으면
# 흠... 질문 게시판 예시들도 다 잘 뜨는데
N, M, B = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

minTime = int(1e9)
result = 257

for i in range(256, -1, -1):
    time = 0
    block = B

    for x in range(N):
        for y in range(M):
            condition = arr[x][y] - i

            # 블록을 파낼 경우
            if condition >= 0: 
                time += 2 * condition
                block += condition
            # 블록을 쌓을 경우
            else:
                # 남은 블록이 없을 경우
                if abs(condition) > block: 
                    time = int(1e9)
                else: 
                    time += abs(condition)
                    block -= abs(condition)

    if time < minTime:
        minTime = time
        result = i

print(minTime, result)

# 정답
import sys
N, M, B = map(int,input().split())
block = []
for _ in range(N):
    block.append([int(x) for x in sys.stdin.readline().rstrip().split()])

ans = int(1e9)
glevel = 0

for i in range(257): #땅 높이
    use_block = 0
    take_block = 0
    for x in range(N):
        for y in range(M):
            # 땅을 파야할 경우
            if block[x][y] > i:
                take_block += block[x][y] - i
            else:
                use_block += i - block[x][y]

    # 여기가 나랑 다른가?
    # 질문 게시판 보니까 이렇게 블럭 개수 체크를 모든 작업 끝난 뒤에 해야된다는데
    # 이럼 문제가 잘못된거지
    # use_block < take_block + B 여도 어느 순간에는 사용한 블럭이 더 많았던 시간대가 있을수도 있는데
    # 게임 고증이 똑바로 안된거지 이건
    # 난 내가 맞다고 봅니다
    if use_block > take_block + B:
        continue

    count = take_block * 2 + use_block

    if count <= ans:
        ans = count
        glevel = i

print(ans, glevel)