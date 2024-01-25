from itertools import product
from collections import deque

picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

def solution(picks, minerals):
    answer = 1e9
    minerals_queue = deque(minerals)

    pick_arr = []
    for i in range(3):
        for _ in range(picks[i]):
            if i == 0: pick_arr.append('dia')
            elif i == 1: pick_arr.append('iron')
            else: pick_arr.append('stone')

    for data in product(pick_arr, repeat=sum(picks)):
        result = 0

        for pick in data:
            cnt = 0
            
            while True:
                if cnt == 5 or len(minerals_queue) == 0:
                    break

                cnt += 1
                mineral = minerals_queue.popleft()

                if pick == 'dia': result += 1
                
                elif pick == 'iron':
                    if mineral == 'diamond': result += 5
                    else: result += 1

                else:
                    if mineral == 'diamond': result += 25
                    elif mineral == 'iron': result += 5
                    else: result += 1

        answer = min(answer, result)

    return answer

print(solution(picks, minerals))

# 정답
# 아.. 곡괭이가 랜덤이어도 된다는건 곡괭이랑 광물 다 랜덤이어도 상관없다는 뜻이구나...
# 그럼 그냥 광물들을 다이아, 철, 돌 순서로 정렬해서 다이아 곡괭이부터 쓰면 되네
# 걍 계산 문제네
def solution(picks, minerals):
    answer = 0
    sum = 0
    # 곡괭이의 수를 구한다.
    for i in picks:
        sum += i
    
    #곡괭이로 캘 수 있는 광물만큼 자른다.
    num = sum * 5
    if len(minerals)>sum:
        minerals = minerals[:num]
    
    #광물들을 조사한다.
    new_minerals =[[0, 0, 0] for _ in range((len(minerals) // 5 +1))]
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            new_minerals[i // 5][0] += 1
        elif minerals[i]=='iron':
            new_minerals[i // 5][1] += 1
        elif minerals[i]=='stone':
            new_minerals[i // 5][2] += 1
    
    #광물의 순서를 다이아몬드, 철, 돌 순서대로 정렬해준다.
    new_minerals.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    
    #정렬된 광물들을 다이아,철,돌 곡괭이 순서대로 캔다.
    for i in new_minerals:
         dia, iron, stone = i
         for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += dia + iron + stone
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += (5 * dia) + iron + stone
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += (25 * dia) + (5 * iron) + stone
                break
    
    return answer