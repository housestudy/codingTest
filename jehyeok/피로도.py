from itertools import permutations

k = 80
dungeons = [[80,20],[50,40],[30,10]]

def solution(k, dungeons):
    answer = -1

    for tmps in permutations(dungeons, len(dungeons)):
        result = 0
        peerodo = k

        for dungeon in tmps:
             if peerodo >= dungeon[0]:
                  peerodo -= dungeon[1]
                  result += 1

        answer = max(answer, result)
        
    return answer

print(solution(k, dungeons))