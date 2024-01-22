# 실패......
# from collections import deque
#
# def cal_tired(pick, mineral):
#     if pick == 'diamond':
#         return 1
#     if pick == 'iron':
#         if mineral == 'diamond':
#             return 5
#         else:
#             return 1
#     if pick == 'stone':
#         if mineral == 'diamond':
#             return 25
#         elif mineral == 'iron':
#             return 5
#         else:
#             return 1

# def solution(picks, minerals):
#     answer = 0
#     mineral_queue = deque(minerals)
#     while mineral_queue:
#         for i in range(3):
#             pick_list = deque()
#             if picks[i] != 0:
#                 picks[i] -= 1
#                 if i == 0:
#                     pick_list.extend(['diamond'] * 5)
#                 elif i == 1:
#                     pick_list.extend(['iron'] * 5)
#                 elif i == 2:
#                     pick_list.extend(['stone'] * 5)
#                 while pick_list and mineral_queue:
#                     answer += cal_tired(pick_list.popleft(), mineral_queue.popleft())
#         if sum(picks) == 0:
#             break
#     return answer
def solution(picks, minerals):
    sum = 0
    for x in picks:
        sum += x

    num_min = sum * 5
    if len(minerals) > num_min:
        minerals = minerals[:num_min]

    cnt_min = [[0, 0, 0] for x in range(10)]  # dia, iron, stone
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            cnt_min[i // 5][0] += 1
        elif minerals[i] == 'iron':
            cnt_min[i // 5][1] += 1
        else:
            cnt_min[i // 5][2] += 1

    sorted_cnt_min = sorted(cnt_min, key=lambda x: (-x[0], -x[1], -x[2]))

    answer = 0
    for mineral in sorted_cnt_min:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p] > 0:  # dia 곡괭이
                picks[p] -= 1
                answer += d + i + s
                break
            elif p == 1 and picks[p] > 0:  # iron 곡괭이
                picks[p] -= 1
                answer += 5 * d + i + s
                break
            elif p == 2 and picks[p] > 0:  # stone 곡괭이
                picks[p] -= 1
                answer += 25 * d + 5 * i + s
                break

    return answer

# 주의 - 곡괭이가 2개 이상일 때, 연속으로만 사용할 수 있는게 아니라 다른 곡괭이 사용 가능 => 그리디 사용?
# mineral 에서 하나씩 빼면서 picks를 하나씩 검사
# 이 때, mineral을 하나씩 빼는 횟수는 5번!
#picks = [1, 3, 2]
#minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
picks = [0, 1, 1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(solution(picks,minerals))

