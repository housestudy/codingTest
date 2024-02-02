def solution(k, dungeons):
    answer = [0]
    length = len(dungeons)

    select = [0 for _ in range(length)]
    taken = [False for _ in range(length)]
    def calanswer(stamina):
        temp = 0
        for sel in select :
            if dungeons[sel][0] <= stamina :
                temp += 1
                stamina -= dungeons[sel][1]
        if answer[-1] < temp:
            answer.pop()
            answer.append(temp)
        return

    def backTrack(idx):
        if idx == length:
            stamina = k
            calanswer(stamina)
        for j in range(length):
            if taken[j] == False:
                select[idx] = j
                taken[j] = True
                backTrack(idx + 1)
                taken[j] = False
        return
    
    backTrack(0)
    return answer[-1]