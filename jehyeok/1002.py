# 내 정답
# ...뭔데
import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

    # 만나지 않을 경우
    # 서로 외부에서 만나지 않을때랑 내부에서 만나지 않을때
    if (distance > r1 + r2) or (abs(r1 - r2) > distance):
        print(0)
    # 외접할 경우
    elif distance == r1 + r2:
        print(1)
    # 내접할 경우
    elif distance == max(r1, r2) - min(r1, r2):
        print(1)
    # 두 점에서 만날 경우
    elif abs(r1 - r2) < distance < r1 + r2:
        print(2)
    # 개수가 무한대일 케이스가 뭔소린지는 모르겠는데...
    else:
        print(-1)

# 답... 개수가 무한대일 케이스가 두 원이 겹칠때구나
# 그것만 고치면 되겠네
# 수학 선생님 자존심좀 세우나 했더만 ㅋㅋ
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

    # 만나지 않을 경우
    # 서로 외부에서 만나지 않을때랑 내부에서 만나지 않을때
    if (distance > r1 + r2) or (abs(r1 - r2) > distance):
        print(0)
    # 외접할 경우
    elif distance == r1 + r2:
        print(1)
    # 내접할 경우
    elif distance == max(r1, r2) - min(r1, r2):
        # 두 원이 겹칠 경우
        if r1 == r2:
            print(-1)
        else:
            print(1)
    # 두 점에서 만날 경우
    elif abs(r1 - r2) < distance < r1 + r2:
        print(2)