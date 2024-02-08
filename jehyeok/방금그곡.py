m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def solution(m, musicinfos):
    answer = ''
    
    titles = []
    musics = []

    m = str(m).replace('C#', 'c').replace('D#', 'd').replace('A#', 'a').replace('G#', 'g').replace('F#', 'f')

    for idx, musicinfo in enumerate(musicinfos):
        totalMusic = ''

        start, end, title, music = musicinfo.split(',')

        startTime = int(start.split(':')[0]) * 60 + int(start.split(':')[1])
        endTime = int(end.split(':')[0]) * 60 + int(end.split(':')[1])
        time = endTime - startTime

        music = str(music).replace('C#', 'c').replace('D#', 'd').replace('A#', 'a').replace('G#', 'g').replace('F#', 'f')
        
        titles.append(title)

        remain = time
        while remain > 0:
            if remain >= len(music):
                totalMusic += music
                remain -= len(music)
            else:
                totalMusic += music[0:remain]
                remain = 0
        
        musics.append(totalMusic)
    
    for idx, music in enumerate(musics):
        if m in music: answer = titles[idx]

    if answer == '': answer = '(None)'

    return answer

print(solution(m, musicinfos))