def time_c(t):		# 시간계산
    return int(t.split(':')[0])*60 + int(t.split(':')[1])

def change(x):		# #음 치환
    exc = {'C#':'1','D#':'2', 'F#':'3', 'G#':'4', 'A#':'5'}
    for k, v in exc.items():
        x = x.replace(k, v)
    return x

def solution(m, musicinfos):
    answer = []
    for info in musicinfos:
        info = info.split(',')
        info[3] = change(info[3])
        T = time_c(info[1]) - time_c(info[0])	# 시간계산
        
        if T >= len(info[3]):	# 시간이 길이보다 길면
            M = info[3] * (T//len(info[3])) + info[3][:T%len(info[3])]
        else:					# 시간이 길이보다 짧으면
            M = info[3][:T]
        
        if change(m) in M:		# 들은음이 있으면 /// in 함수를 사용하면 백준에서 시간초과가 나오는 경우가 많았어서 잘 이용안했는데
            answer.append([T, info[2]]) # 이건 반복하는 구조다 보니 매우 빠르게 적용되는 것 같더군요.
        
    if len(answer) == 0:
        return '(None)'
    else:
        return sorted(answer, key=lambda x: -x[0])[0][1] # sorted 메커니즘이 동일한 시간인 경우에 앞선 idx 에 있는 녀석이 그대로 유지 되는 메커니즘인지 확인할 필요가 있어보이네요.