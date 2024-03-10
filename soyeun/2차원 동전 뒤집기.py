# bfs
# heapq ((뒤집은 횟수, 현재 그래프 상태))
# 가능한 모든 경우를 heapq에 넣기
# 1) 1,2,3,...행 뒤집은 각각의 경우, 1,2,3,... 열을 뒤집은 각각의 경우
# 목표 상태와 같아지면 스탑
# => 시간 초과

import heapq
def row_change(row_num, graph):
    n = len(graph[row_num])
    for i in range(n):
        if graph[row_num][i] == 0:
            graph[row_num][i] = 1
        else:
            graph[row_num][i] = 0
    #print('changed_graph:',graph)
    return graph

def column_change(column_num, graph):
    n = len(graph)
    for i in range(n):
        if graph[i][column_num] == 0:
            graph[i][column_num] = 1
        else:
            graph[i][column_num] = 0
    return graph



def solution(beginning, target):
    n = len(beginning)
    m = len(beginning[0])
    heap = []

    for row in range(n):
        graph = [row.copy() for row in beginning]
        graph = row_change(row, graph)
        heapq.heappush(heap,(0,graph))
    for column in range(m):
        graph = column_change(column,graph)
        heapq.heappush(heap,(0,graph))
    while heap:
        cnt, cur_graph = heapq.heappop(heap)
        print('cnt',cnt)
        print('cur_graph',cur_graph)
        if cur_graph == target:
            return cnt
        else:
            for row in range(n):
                graph = row_change(row, cur_graph)
                heapq.heappush(heap, (cnt+1, graph))
            for column in range(m):
                graph = column_change(column, cur_graph)
                heapq.heappush(heap, (cnt+1, graph))
    return -1


beginning = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

#print(solution(beginning, target))
n = len(beginning)
for i in range(n):
    num1 = int(''.join(beginning[i]),2)
    num2 = int(''.join(target[i]),2)
    print(bin(num1^num2))

