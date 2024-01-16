import heapq
def solution(jobs):
    # answer : 작업 요청부터 작업 종료까지 걸린 시간
    # now : 현재 시간
    # i : 작업 한 횟수
    answer, now, i = 0, 0, 0

    # start : 이전 작업이 끝난 시간
    start = -1

    heap = []
    while i < len(jobs):
        for job in jobs:
            # 요청 시간이 현재 시간보다 작거나 같아야 함, 이전 시작 시간보다 커야함
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
        else:
            now += 1
    return answer // len(jobs)

#[0,3] -> [3,9] -> [9,18]

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
