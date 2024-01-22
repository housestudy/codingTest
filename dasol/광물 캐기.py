def solution(picks, minerals):
    # 미네랄은 조건 순서대로만 캘 수 있음.
    graph = [[1, 1, 1], [5, 1, 1], [25, 5, 1]] # 행은 곡괭이 종류 다/철/아, 열은 광물 다/철/아
    length = len(minerals)
    pick_capa = 5*sum(picks)
    efforts_sum = []
    temp = [0, 0, 0] # 다/철/아 순으로 드는 에포트 값 (5개마다)
    count = 0
    idx = 0
    if length < pick_capa :
        limit = length
        flag = True
    else:
        limit = pick_capa
        flag = False
    while idx < limit:
        count += 1
        if minerals[idx] == "diamond":
            mineral = 0
        elif minerals[idx] == "iron":
            mineral = 1
        else:
            mineral = 2
        for i in range(3):
            temp[i] += graph[i][mineral]
        if count == 5:
            efforts_sum.append(temp)
            temp = [0, 0, 0]
            count = 0
        idx += 1
    if flag :
        efforts_sum.append(temp)
    efforts_sum.sort(key= lambda x : (-x[2], -x[1], x[0]))
    answer = 0
    j = 0
    for effort in efforts_sum :
        while True:
            if picks[j] != 0:
                picks[j] -= 1
                answer += effort[j]
                break
            else:
                j += 1
    return answer 