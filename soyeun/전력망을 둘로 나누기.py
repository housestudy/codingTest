from collections import deque

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start):

        visited = [0] * (n + 1)
        q = deque([start])
        visited[start] = 1
        cnt = 1
        while q:
            s = q.popleft()

            for i in graph[s]:
                if visited[i] == 0:
                    visited[i] = 1
                    cnt += 1
                    q.append(i)

        return cnt

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        answer = min(abs(bfs(a)-bfs(b)),answer)

        graph[a].append(b)
        graph[b].append(a)

    return answer
n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n,wires))