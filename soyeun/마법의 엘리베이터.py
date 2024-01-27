def solution(storey):
    answer = 0
    value = storey
    while True:
        value,remainder = divmod(value,10)
        if remainder == 0 and value == 0:
            break
        if remainder <= 4:
            answer += remainder
        elif remainder >= 6:
            answer += (10-remainder)
            value += 1
        elif remainder == 5:
            if int(str(value)[-1]) > 4:
                answer += remainder
                value += 1
            else:
                answer += remainder
    return answer
