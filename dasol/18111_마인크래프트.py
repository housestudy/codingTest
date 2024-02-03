import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())

ground = []
targetHeight = 256
answer = [2*256*n*m,257]
for i in range(n):
    ground.append(list(map(int, input().split())))

while targetHeight >= 0:
    placedBlock = 0
    removedBlock = 0
    for i in range(n):
        for j in range(m):
            curr = ground[i][j]
            if curr < targetHeight:
                placedBlock += targetHeight - curr
            elif curr > targetHeight:
                removedBlock += curr - targetHeight

    # 밑에 이렇게 비교하는 경우는, 우리가 블럭을 순회할 때, 한 개의 칸을 다 완료하고 나서 움직여야 한다는 조건이 없기
    # 때문에, 인벤토리에 현재는 0개여도, 다른데거 하나 깎아서 가져온담에 하나 놓고 하는식으로 해도 되는게 맞는 것 같네요.
    # 근데 이런식으로 짜면, 칸 사이를 이동하는 시간은 무시된다는 뜻이니까 게임 고증이 제대로 안된게 맞다.
    if placedBlock <= removedBlock + b :
        total_time = placedBlock + removedBlock*2
        if answer[0] > total_time:
            answer[0] = total_time
            answer[1] = targetHeight
    targetHeight -= 1

print(*answer)