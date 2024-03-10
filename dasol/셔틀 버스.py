def solution(n, t, m, timetable):
    timeline = []
    for time in timetable:
        hr, min = map(int, time.split(":"))
        timeline.append(hr*60 + min)
    timeline.sort(reverse = False)

    firstdeparture = 540
    shutletable = [firstdeparture]
    for i in range(n-1):
        firstdeparture += t
        shutletable.append(firstdeparture)

    # 사람 기준으로 탐색해보자 / 사람 기준도 옳지 않다. 사람 기준으로 하면 kone이 무조건 회사에 도착한다는 기준이 충족되지 않을 수 있음
    # 즉 사람과 셔틀 두가지 기준을 모두 충족시켜야 함. info를 기준으로 사람을 + 셔틀을 기준으로 돌리자.
    
    kone = 0
    i = 0
    for dt in shutletable:
        cnt = 0
        while cnt < m and i < len(timeline) and timeline[i] <= dt :
            i+=1
            cnt += 1
        if cnt < m : kone = dt
        else: kone = timeline[i-1]-1
    answer = "{0:02d}:{1:02d}".format(kone//60, kone%60)
    return answer


print(solution(2,1,2, ["09:00", "09:00", "09:00", "09:00"]))