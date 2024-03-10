# 백트래킹 마지막

# 이건 너무 쉽다
N, M = map(int, input().split())
arr = []

def back():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, N + 1):
        arr.append(i)
        back()
        arr.pop()

back()