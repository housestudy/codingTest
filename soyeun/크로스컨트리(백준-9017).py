from collections import defaultdict, Counter

T = int(input())
answer = []
for _ in range(T):
    n = int(input())
    result = defaultdict(lambda: [0,0,0])
    team_num = list(map(int, input().split()))
    team_count = Counter(team_num)
    score = 1
    for index in range(n):
        team = team_num[index]
        result[team][0] += 1
        if team_count[team] < 6:
            result[team][1] = float('inf')
            continue
        if result[team][0] <= 4:
            result[team][1] += score
        elif result[team][0] == 5:
            result[team][2] = score
        score += 1
    sorted_result = dict(sorted(result.items(), key = lambda x:(x[1][1],x[1][2])))
    answer.append(list(sorted_result.keys())[0])
for ans in answer:
    print(ans)