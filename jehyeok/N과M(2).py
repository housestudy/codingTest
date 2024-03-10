# 백트래킹 2번~

# 오 쒸 이게 맞네 ㅋㅋ
N, M = map(int, input().split())
arr = []

def back(t):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(t + 1, N + 1):
        if i not in arr:
            arr.append(i)
            back(i)
            arr.pop()

back(0)