def solution(topping):
    big_bro = [0 for _ in range(10001)]
    sml_bro = [0 for _ in range(10001)]
    length = len(topping)
    big = 0
    sml = 0
    answer = 0
    for i in range(length):
        tmp = topping[i]
        if sml_bro[tmp] == 0:
           sml_bro[tmp] += 1
           sml += 1
        else:
            sml_bro[tmp] += 1

    for i in range(length):
        tmp = topping[i]
        if big_bro[tmp] == 0 :
            big_bro[tmp] += 1
            sml_bro[tmp] -= 1
            big += 1
            if sml_bro[tmp] == 0:
                sml -= 1
        else:
            big_bro[tmp] += 1
            sml_bro[tmp] -= 1
            if sml_bro[tmp] == 0:
                sml -= 1
        if big == sml :
            answer += 1
    return answer