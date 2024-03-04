# 목적지에 도착하지 못하는 경우를 구해주기

from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    def manhatton(x1, y1):
        return abs(x1-(r-1))+abs(y1-(c-1))

    # k가 최단 거리보다 작거나, k-최소 거리가 홀수일 경우 도착점에 도착 못함
    if manhatton(x-1,y-1) > k or (manhatton(x-1,y-1)-k)%2:
        return 'impossible'

    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    ds = ['d','l','r','u']

    queue = deque()
    queue.append([x-1,y-1,0,""])
    while queue:
        temp_x, temp_y, cnt, s = queue.popleft()

        # 도착시 남은 거리가 홀수일 경우
        if temp_x == r-1 and temp_y == c-1 and (k-cnt)%2:
            return 'impossible'

        elif temp_x == r-1 and temp_y == c-1 and cnt == k:
            return s

        for i in range(4):
            cur_x = temp_x + dx[i]
            cur_y = temp_y + dy[i]
            if cur_x >= 0 and cur_x < n and cur_y >= 0 and cur_y < m:
                # 남은 거리 + 현재까지 이동 거리가 k보다 큰 경우 넘어감
                if manhatton(cur_x,cur_y) + cnt + 1 > k:
                    continue
                queue.append([cur_x,cur_y,cnt+1,s+ds[i]])
                break
    return answer










# 내 풀이
# bfs 풀이
# n*m의 그래프 생성 => 중복 방문 가능하므로 만들 필요 없을듯
# 상하좌우 순서대로 넣기
# 큐에 넣을 때, 문자열과 이동 횟수, 좌표를 함께 넣기
# 시간 초과 발생 => k가 클 때, 해결 방안이 필요

# from collections import deque
#
# def solution(n, m, x, y, r, c, k):
#     answer_list = []
#
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]
#     ds = ['u','d','l','r']
#
#     queue = deque()
#     queue.append(['',0,x-1,y-1])
#
#     while queue:
#         s, cnt, tmp_x,tmp_y = queue.popleft()
#         if cnt == k:
#             if tmp_x == r-1 and tmp_y == c-1:
#                 answer_list.append(s)
#         elif cnt < k:
#             for i in range(4):
#                 cur_x = tmp_x + dx[i]
#                 cur_y = tmp_y + dy[i]+
#                 if cur_x >= 0 and cur_x < n and cur_y >= 0 and cur_y < m:
#                     queue.append([s + ds[i], cnt + 1, cur_x, cur_y])
#
#     if len(answer_list) == 0:
#         return "impossible"
#
#     answer_list.sort()
#     return answer_list[0]
n = 3
m = 4
x = 2
y = 3
r = 3
c = 1
k = 5
# n = 3
# m = 3
# x = 1
# y = 2
# r = 3
# c = 3
# k = 4
print(solution(n, m, x, y, r, c, k))










