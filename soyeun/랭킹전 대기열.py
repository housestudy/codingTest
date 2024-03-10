# 풀이 참고
# 1. {방 번호 : [가능한 레벨의 최소값, 가능한 레벨의 최대값]}인 dict 생성
# 2. 플레이어들의 레벨과 아이디를 하나씩 가져오기
# 3. 1번의 dict를 이용하여 레벨을 비교하여 해당 방 번호에 넣기
# 3-1. 이 때, 해당 방의 플레이어 수가 m이면 다음 방에 넣기
# 플레이어를 각 방에 넣을 때는 [[0번방],[1번방]...] 형식으로 넣기

from collections import defaultdict
# 플레이어의 수, 방의 정원
p, m = map(int, input().split())
room_dict = defaultdict(list)
result = []

for _ in range(p):
    level, nickname = input().split()
    level = int(level)

    if len(room_dict) == 0:
        room_dict[0].append(level-10)
        room_dict[0].append(level+10)
        result.append([[level,nickname]])

    else:
        ch = False
        for index in range(len(room_dict)):
            min_level = room_dict[index][0]
            max_level = room_dict[index][1]
            # 각 방을 탐색하면서 조건에 맞으면 넣기
            if min_level <= level and level <= max_level and len(result[index]) < m:
                result[index].append([level, nickname])
                ch = True
                break

        # 아무 방에도 못 들어간 경우
        if ch == False:
            room_dict[index+1].append(level-10)
            room_dict[index+1].append(level + 10)
            result.append([[level, nickname]])

for res in result:
    sorted_res = sorted(res, key = lambda x:x[1])
    if len(sorted_res) == m:
        info = 'Started!'
    else:
        info = 'Waiting!'

    print(info)
    for level, nick in sorted_res:
        print(level, nick)

