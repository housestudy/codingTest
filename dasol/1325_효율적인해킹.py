import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 딕셔너리로 직접 만들어주는 풀이방식 (시간초과)
# trust = dict() # 내가(key) 신뢰하는 딕셔너리 세트
# trusted = dict() # 나를(key) 신뢰하는 딕셔너리 세트
# count = [0 for _ in range(N+1)]

# def trusted_dfs(key, value):
#     if key in trusted:
#         temp = trusted[key]
#         temp.add(value)
#         trusted[key] = temp
#     else:
#         trusted[key] = {value}

#     if key in trust:
#         for i in trust[key]:
#             trusted_dfs(i, value)
#     return

# def trust_dfs(key, value):
#     if key in trust:
#         temp = trust[key]
#         temp.add(value)
#         trust[key] = temp
#     else:
#         trust[key] = {value}
#     return


# for i in range(M):
#     a, b = map(int, input().split()) # a가 b를 신뢰한다. / b를 해킹하면 a도 해킹 가능하다.
#     # 논리를 적어봅시다.
#     # 내 '가' 신뢰하는 리스트를 작성하고
#     # 나 '를' 신뢰하는 리스트를 작성한다.
#     # 근데 이때, 신뢰받는 주체가 다른 객체(C)를 신뢰하고 있으면, C가 신뢰하는 애들한테는 다 추가해줘야 한다.
#     trust_dfs(a,b)
#     trusted_dfs(b,a)

# for i,j in trusted.items():
#     count[i] += len(j)

# number_list = []
# max_hack = 0
# for i in range(1, N+1):
#     if max_hack < count[i]:
#         max_hack = count[i]
#         number_list = []
#         number_list.append(i)
#     elif max_hack == count[i]:
#         number_list.append(i)
# result = " ".join(map(str, number_list))
# print(result)




# 그래프로 연결관계 표현하고 탐색하는 방식. 근데 메모리 초과 떴다. 그래프를 만드는 방식이 잘못 됐나? N * N 크기
# 말고 더 작게 그냥 일반 리스트 방식으로 만들까.

# graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
# # count = [0 for _ in range(N+1)]

# for i in range(M):
#     a, b = map(int, input().split())
#     graph[a][b] += 1

# def add_dfs(e):
#     # count[e] += 1
#     graph[e][e] += 1
#     for k in range(1, N+1):
#         if graph[e][k] :
#             add_dfs(k)
#     return

# for i in range(1,N+1):
#     for j in range(1, N+1):
#         if graph[i][j] :
#             add_dfs(j)

# answer_list = []
# max_hack = 0
# # for i in range(1,N+1):
# #     if count[i] > max_hack:
# #         max_hack = count[i]
# #         answer_list = []
# #         answer_list.append(i)
# #     elif count[i] == max_hack:
# #         answer_list.append(i)
# for i in range(1,N+1):
#     if graph[i][i] > max_hack:
#         max_hack = graph[i][i]
#         answer_list = []
#         answer_list.append(i)
#     elif graph[i][i] == max_hack:
#         answer_list.append(i)
# result = " ".join(map(str, answer_list))
# print(result)





# dlsajhgofaspedjgoi90-4wIUT90i%()*i#_@q*i^%_(i@_^)#$i(%) 개빡친다 진심... BFS 인건 알겠는데, 
# 뭐가 바뀐건지 pypy로 돌려야지만 답이 통과됐다. 장난하냐?

from collections import deque

graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

# bfs
ans = []
for i in range(1, N+1):
    visited = [False]*(N+1)
    queue = deque([i])
    visited[i] = True
    
    cnt = 1
    while queue:
        x = queue.popleft()
        for j in graph[x]:
            if not visited[j]:
                visited[j] = True
                queue.append(j)
                cnt += 1
    ans.append(cnt)

max_cnt = max(ans)
for i in range(N):
    if ans[i] == max_cnt:
        print(i+1, end=" ")