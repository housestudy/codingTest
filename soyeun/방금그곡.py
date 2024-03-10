def solution(m, musicinfos):
    answer = ''
    n = len(m) - m.count('#')
    max_play = 0
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        info = []
        for i in range(len(music)):
            if music[i] == '#':
                info[-1] += '#'
            else:
                info.append(music[i])
        play_time = (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:]))
        a, b = divmod(play_time, len(info))
        final_info = info * a + info[:b]

        for index in range(len(final_info) - n + 1):
            temp_final = ''.join(final_info[index:index + n])
            if temp_final == m:
                if play_time > max_play:
                    max_play = play_time
                    answer = title
    if answer == '':
        answer = '(None)'
    return answer