# 1. timetable을 정수화하여 정렬
# 2. 셔틀버스가 오는 시간도 정수화하여 저장
# 3. 셔틀 버스 도착 시간에 따라 해당 값보다 작은 대기열의 개수 세기
# 4. 이때, m명보다 작고 index 값은 전체 크루 수보다 작아야 함
# 5. 탈 수 있는 크루의 수가 m명보다 작을 때, 버스 도착 시간에 도착해도됨
# 6. m명보다 클 때, 마지막 크루의 도착 시간보다 1분 빨리와야함

def solution(n, t, m, timetable):
    answer = ''
    timetable_list = [int(time.split(':')[0])*60 + int(time.split(':')[1]) for time in timetable]
    timetable_list.sort()
    shuttle_bus = [9*60 + i*t for i in range(n)]

    index = 0
    for shuttle in shuttle_bus:
        cnt = 0
        while index < len(timetable_list) and cnt < m and timetable_list[index] <= shuttle:
            cnt += 1
            index += 1
        if cnt < m:
            answer = shuttle
        else:
            answer = timetable_list[index-1]-1

    answer = str(answer//60).zfill(2) + ':' + str(answer%60).zfill(2)
    return answer

n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n,t,m,timetable))