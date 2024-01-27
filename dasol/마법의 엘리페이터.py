def solution(storey):
    # 백 트래킹으로 풀 수 있었어서 기부니가 매우 좋습니다.ㅋㅋ
    # 백 트래킹으로 풀면 5를 기준으로 나누는 연산이 필요 없습니다. 그냥 단순 비교만 하면 됩니다.
    # N-퀸은 백트랙킹 중에서도 최상위 문제이고, 제가 추천드린 N과M은 백트래킹 기본예제 입니다.
    # N과 M을 시도해보시고 이 문제 시도해보시면 아주 좋을 것 같습니다.
    numbers = [0] + list(map(int, str(storey)))
    length = len(numbers)
    temp = 0
    answer = []
    answer.append(storey)
    # flag 는 낮은 자리 숫자에서 올림이 됐는지 안됐는지 확인하는 용도
    def backtrack(idx, temp, flag):
        # numbers 리스트에 0을 앞에 추가해두었기 때문에, numbers[0] 은 무조건 0 이지만, 낮은 자리에서 올림됐으면
        # 1만큼만 더해주고 정답리스트에 추가했습니다.
        if idx == 0:
            if flag :
                answer.append(temp+1)
                return
            answer.append(temp)
            return
        if temp > min(answer):
            return
        # 올림되었을 떄는 지금 자릿수가 10이 되는지 확인해봐야 함. 10이 되면 지금이랑 상관없이 바로 다음 자리 숫자로 넘김
        if flag :
            if numbers[idx] + 1 != 10:
                temp += numbers[idx] +1
                backtrack(idx - 1, temp, 0)
                temp += 10 - 2*(numbers[idx] + 1)
                backtrack(idx - 1, temp, 1)
            else:
                backtrack(idx - 1, temp, 1)
                return
        # 올림 안되었을 때는 올림/내림 둘 다 dfs로 돌림
        else:
            temp += numbers[idx]
            backtrack(idx - 1, temp, 0)
            temp += 10 - 2*numbers[idx]
            backtrack(idx - 1, temp, 1)

    backtrack(length-1, temp, 0)

    return min(answer)