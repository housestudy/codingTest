# dfs 활용(재귀)
# dfs 종료 조건 : dfs(index)에서 index가 M 이상일 때
def dfs(index):
    if index >= m:
        for ans in answer:
            print(ans, end=' ')
        print()
        return
    else:
        for i in range(1,n+1):
            if ch[i] == 0:
                answer[index] = i
                ch[i] = 1
                dfs(index+1)
                answer[index] = 0
                ch[i] = 0

n, m = map(int, input().split())
answer = [0] * m
ch = [0] * (n+1)

dfs(0)
