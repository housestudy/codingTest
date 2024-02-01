# import sys
# from collections import deque

# input = sys.stdin.readline

# p, m = map(int, input().split())

# rooms = [[[0, 0]] for _ in range(501)]
# answers = []

# # 동일한 레벨에 다 차있어서 시작했는데 새로 만들때 문제가 생길 수 있으면, answers로 flushing을 하면 되지 뭐.
# roomCount = 0
# for _ in range(p):
#     l, n = input().split()
#     l = int(l)
#     isRoom = False
#     whichRoom = 501
#     left, right = l-10, l + 11
#     if left <= 0 : left = 1
#     if right > 500: right = 501
#     for i in range(left, right):
#         if 0 < rooms[i][0][1] < m and rooms[i][0][0] != 0 :
#             isRoom = True
#             whichRoom = min(whichRoom, i)
#     if isRoom:
#         rooms[whichRoom].append([l, n])
#         rooms[whichRoom][0][1] += 1
#         if rooms[whichRoom][0][1] == m:
#             temp = deque([])
#             for member in rooms[whichRoom]:
#                 temp.append(member)
#             answers.append(temp)
#             rooms[whichRoom] = [[0,0]]
#     else:
#         roomCount += 1
#         rooms[l][0][0] = roomCount
#         rooms[l][0][1] += 1
#         rooms[l].append([l,n])

# rooms.sort(key= lambda x: -x[0][0])

# for room in rooms:
#     if room[0][0] == 0: break
#     else:
#         answers.append(deque(room))

# # 전부다 입장시키고는 방 순서대로 출력
# answers.sort(key= lambda x: (x[0][0]))

# for answer in answers:
#     _ , cnt = answer.popleft()
#     temp = list(answer)
#     temp.sort(key = lambda x: x[1])
#     if cnt == m:
#         print("Started!")
#         for mem in temp:
#             print(*mem)
#     else:
#         print("Waiting!")
#         for mem in temp:
#             print(*mem)


p, m = map(int, input().split())
people = []
for i in range(p):
    lv, id = input().split()
    people.append([int(lv), id])

rooms = []

for lv, id in people:
    flag = False
    for i in range(len(rooms)):
        if len(rooms[i][1]) == m:
            continue
        
        # 들어갈 수 있는 방이 있으면 입장
        if rooms[i][0] - 10 <= lv <= rooms[i][0] + 10:
            flag = True
            rooms[i][1].append([lv, id])
            break
            
    # 대기방에 들어 갈 수 없으면 새로운 방 생성
    if not flag:
        rooms.append([lv, [[lv, id]]])

# 방이 생성된 시간 순서로 출력
for i in range(len(rooms)):
    if len(rooms[i][1]) == m:
        print('Started!')
        tmp_ids = sorted(rooms[i][1], key=lambda x: x[1])
        for j in range(m):
            print(*tmp_ids[j])
    else:
        print('Waiting!')
        tmp_ids = sorted(rooms[i][1], key=lambda x: x[1])
        for j in range(len(tmp_ids)):
            print(*tmp_ids[j])