# https://school.programmers.co.kr/learn/courses/30/lessons/159993
# Lv2.

# 이것도 시간 안에 못풀었네..?
# 시작 지점부터 레버까지 걸리는 시간 + 레버에서 끝까지 걸리는 시간만 결과로 내놓고
# 중간에 못가는 경우에 대한 케이스만 추가하면 되는건데...
# 파이썬을 잘 안쓰니까 문법같은거 찾는데 시간이 너무 오래 걸린다
# 뭐 문자열을 리스트로 변환시키는 법이나, global 변수 사용법이나..

from collections import deque

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

def solution(maps):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    mapsSize = len(maps)
    for i in range(mapsSize):
        maps[i] = list(maps[i])

    global startX, startY, leverX, leverY, endX, endY

    for i in range(mapsSize):
        for j in range(mapsSize):
            if maps[i][j] == 'S':
                startX = i
                startY = j
            if maps[i][j] == 'L':
                leverX = i
                leverY = j
            if maps[i][j] == 'E':
                endX = i
                endY = j

    countingMaps = [[0] * mapsSize for _ in range(mapsSize)]

    def bfs(x, y, desX, desY):
        datas = [(x, y)]
        queue = deque(datas)

        while queue:
            data = queue.popleft()
            x, y = data[0], data[1]

            print(x, y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= mapsSize or ny >= mapsSize or maps[nx][ny] == 'X':
                    continue

                elif countingMaps[nx][ny] == 0:
                    queue.append((nx, ny))

                    countingMaps[nx][ny] = countingMaps[x][y] + 1

        return countingMaps[desX - 1][desY - 1]
    
    answer = bfs(startX, startY, leverX, leverY)

    return answer

print(solution(maps))

# 정답

def bfs(start, end, maps):
	# 탐색할 방향
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]
    
    n = len(maps)       # 세로
    m = len(maps[0])    # 가로
    visited = [[False] * m for _ in range(n)]
    que = deque()
    flag = False
    
    # 초깃값 설정
    for i in range(n):
        for j in range(m):
        	# 출발하고자 하는 지점이라면 시작점의 좌표를 기록함
            if maps[i][j] == start:      
                que.append((i, j, 0))    
                # 별도의 cost 리스트를 만들지 않고 que에 바로 기록(0)
                visited[i][j] = True
                flag = True; break 
                # 시작 지점은 한 개만 존재하기 때문에 찾으면 바로 나옴
        if flag: break
                
    # BFS 알고리즘 수행 (핵심)
    while que:
        y, x, cost = que.popleft()
        
        if maps[y][x] == end:
            return cost
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # maps 범위내에서 벽이 아니라면 지나갈 수 있음
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X':
                if not visited[ny][nx]:	# 아직 방문하지 않는 통로라면
                    que.append((ny, nx, cost+1))
                    visited[ny][nx] = True
                    
    return -1	# 탈출할 수 없다면
        
            
def solution(maps):
    path1 = bfs('S', 'L', maps)	# 시작 지점 --> 레버
    path2 = bfs('L', 'E', maps) # 레버 --> 출구
    
    # 둘다 -1 이 아니라면 탈출할 수 있음
    if path1 != -1 and path2 != -1:
        return path1 + path2
        
   	# 둘중 하나라도 -1 이면 탈출할 수 없음
    return -1