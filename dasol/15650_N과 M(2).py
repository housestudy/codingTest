N, M = map(int, input().split())

numbers = [0] + [0 for _ in range(N)]
answer = ["0" for _ in range(M)]

def sol(n):
    if n == M:
        print((" ").join(answer))
        return
    for i in range(N):
        if numbers[i+1] != 1 :
            if answer[n-1] < str(i+1) :
                answer[n] = str(i+1)
                numbers[i+1] = 1
                sol(n+1)
                numbers[i+1] = 0
                answer[n] = "0"
    return

sol(0)