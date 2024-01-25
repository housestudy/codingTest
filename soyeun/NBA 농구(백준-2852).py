def TimeToNum(time):
    minute, second = map(int, time.split(':'))
    return minute*60 + second
def NumToTime(num):
    minute = str(num//60)
    second = str(num%60)
    if len(minute) == 1:
        minute = '0' + minute
    if len(second) == 1:
        second = '0' + second
    return minute + ':' + second

n = int(input())
score_list = [list(input().split()) for _ in range(n)]
score_dict = dict()
team1_win = 0
team2_win = 0
team1_time = 0
team2_time = 0

for team, time in score_list:
    score_dict[TimeToNum(time)] = team

for i in range(TimeToNum('48:00')):
    if i in score_dict:
        if score_dict[i] == '1':
            team1_win += 1
        else:
            team2_win += 1
    if team1_win > team2_win:
        team1_time += 1
    elif team2_win > team1_win:
        team2_time += 1

print(NumToTime(team1_time))
print(NumToTime(team2_time))