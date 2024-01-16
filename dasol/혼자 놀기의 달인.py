def solution(cards):
    scores = []
    answer = 0
    length = len(cards)
    visited = [0 for _ in range(length)]
    def search(i):
        group_sum = 0
        x = i
        while visited[x] != True:
            visited[x] = True
            x = cards[x]-1
            group_sum += 1
        scores.append(group_sum)
        return
    for i in range(length):
        if visited[i] == False :
            search(i)

    scores.sort(reverse= True)    
    answer = scores[1] * scores[0] if len(scores) > 1 else 0
    return answer