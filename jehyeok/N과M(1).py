# 백트래킹 1번!
# 요건 일단 백트래킹 공부니까 답 그대로

N, M = map(int, input().split())
arr = []

def back():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, N + 1):
        if i not in arr:
            arr.append(i)
            back()
            arr.pop()

back()