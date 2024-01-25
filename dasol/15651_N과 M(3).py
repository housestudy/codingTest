N, M = map(int, input().split())

numbers = [0 for _ in range(M)]

def tracking(idx):
    if idx == M:
        print(*numbers)
    else:
        for i in range(1,N+1):
            numbers[idx] = i
            tracking(idx + 1)
    return

tracking(0)