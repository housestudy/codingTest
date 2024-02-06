import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def sol(n, tmp):
    global bigNum, smallNum

    if n == N-1:
        if tmp > bigNum:
            bigNum = tmp
        if tmp < smallNum:
            smallNum = tmp
        return
    
    for i in range(4):
        if cal[i] > 0:
            cal[i] -= 1
            if i == 0:
                sol(n+1, tmp + numbers[n+1])
                cal[i] += 1
            elif i == 1:
                sol(n+1, tmp - numbers[n+1])
                cal[i] += 1
            elif i == 2:
                sol(n+1, tmp * numbers[n+1])
                cal[i] += 1
            else:
                if tmp > 0 :
                    sol(n+1, tmp//numbers[n+1])
                    cal[i] += 1
                else:
                    sol(n+1, -(abs(tmp)//numbers[n+1]))
                    cal[i] += 1

N = int(input())
numbers = list(map(int, input().split()))
cal = list(map(int, input().split()))

bigNum = -1e9
smallNum = 1e9

sol(0, numbers[0])
print(bigNum)
print(smallNum)