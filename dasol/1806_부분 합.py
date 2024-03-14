import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(1,N):
    nums[i] = nums[i-1] + nums[i]

def sol():
    result = 100000
    for i in range(N-1, 0, -1):
        k = 1
        while True:
            if nums[i] - nums[i-k] >= S:
                if result > k :
                    result = k
                    break
            if i-k < 0 :
                break
            k+=1
            if k > result:
                break
    if nums[0] >= S:
        return 1
    if nums[N-1] >= S:
        if result > N:
            return N
    if result == 100000: return 0
    else: return result

print(sol())