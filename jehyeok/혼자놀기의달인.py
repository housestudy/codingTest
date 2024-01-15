# https://school.programmers.co.kr/learn/courses/30/lessons/131130
# Lv 2.

from collections import deque
from copy import deepcopy

cards = [2, 3, 4, 5]

def solution(cards):
    answer = 0

    results = []

    def bfs(start, cards, visited):
        queue = deque([start])
        visited[start] = True

        cnt = 1

        while queue:
            v = queue.popleft()

            if cards[v] > len(cards):
                continue

            if not visited[cards[v] - 1]:
                queue.append(cards[v] - 1)
                visited[cards[v] - 1] = True
                cnt += 1

        return cnt

    for i in range(0, len(cards)):
        visited = [False] * (len(cards) + 1)
        tmp_cards = deepcopy(cards)
        cnt1 = bfs(i, tmp_cards, visited)

        not_visited_cards = [i for i in range(len(tmp_cards)) if visited[i] == False]

        if len(not_visited_cards) == 0:
            results.append(0)
            break

        for x in not_visited_cards:
            cnt2 = bfs(x, tmp_cards, visited)
            results.append(cnt1 * cnt2)

        results.append(cnt1 * cnt2)

    answer = max(results)

    return answer

print(solution(cards))