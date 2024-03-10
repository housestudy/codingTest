from collections import deque

n, t, m = 1, 1, 5
timetable = ["08:00", "08:01", "08:02", "08:03"]	

def solution(n, t, m, timetable):
    answer = ''

    remains = {} # 각 버스 시간에 남은 자리수
    bus_times = [] # 각 버스 시간

    for i in range(n):
        time = 540 + (t * i)
        remains[time] = m
        bus_times.append(time)

    timetable.sort()
    new_timetable = deque([])

    for data in timetable:
        hour, minute = data[0:2], data[3:]
        new_timetable.append((int(hour) * 60) + int(minute))

    for time in bus_times:
        popCnt = remains[time]
        cnt = 0

        for _ in range(popCnt):
            if len(new_timetable) > 0 and new_timetable[0] <= time:
                new_timetable.popleft()
                cnt += 1

        remains[time] -= cnt

    remainKeys = list(remains.keys())
    remainValues = remains.values()

    idx = -1

    for i, v in enumerate(remainValues):
        if v > 0: idx = max(idx, i)

    if idx != -1:
        result = remainKeys[idx]
        hour, minute = result // 60, result % 60

        if hour < 10: hour = '0' + str(hour)
        else: hour = str(hour)

        if minute < 10: minute = '0' + str(minute)
        else: minute = str(minute)

        answer = hour + ":" + minute

    return answer

print(solution(n, t, m, timetable))

# 답
# ㅋㅋ...? 13줄...?
def solution(n, t, m, timetable):
    answer = 0
    # 모든 시간을 분으로 환산해서 생각
    # 예시: "09:10" => 9*60 + 10 = 550(분)
    # 크루 도착 시각 리스트
    crewTime = [int(time[:2])*60 + int(time[3:]) for time in timetable]
    crewTime.sort()
    # 버스 도착 시각 리스트
    busTime = [9*60 + t*i for i in range(n)]

    i = 0       # 다음에 버스에 오를 크루의 인덱스
    for tm in busTime:
      cnt = 0   # 버스에 타는 크루 수
      while cnt < m and i < len(crewTime) and crewTime[i] <= tm:
        i += 1
        cnt += 1
      # 버스에 자리가 남았을 경우
      if cnt < m: answer = tm
      # 버스에 자리가 없는 경우 맨 마지막 크루보다 1분 먼저 도착
      else: answer = crewTime[i - 1] - 1

    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)