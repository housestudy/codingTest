# 오랜만에 백준~ 1461번

# 내 정답
# 코드 봐라 미쳤다 속도 개빠를듯
N, M = map(int, input().split())

data = list(map(int, input().split()))
data.sort() # 데이터 정렬

negative_data = [x for x in data if x < 0] # 음수 값
positive_data = [x for x in data if x > 0] # 양수 값

negative_len = len(negative_data)
positive_len = len(positive_data)

result = 0

# 모든 데이터 중 절대값이 가장 큰 데이터의 경우 마지막엔 돌아올 필요가 없기 때문에...
# 근데 그냥 절대값으로만 계산하면 이게 음수값인지.. 양수 값인지 모르겠음
if negative_len == 0: # 음수 값이 없을 경우
    result += positive_data[-1] # 양수 값 중 가장 큰 값을 더해주고
    positive_data = positive_data[:positive_len - M] # 뒤에서부터 M 개만큼 빼고 나머지를 positive_data에 저장
elif positive_len == 0: # 양수 값이 없을 경우
    result += -negative_data[0] # 음수 값 중 절대값이 가장 큰 값의 절대값을 더해주고
    negative_data = negative_data[M:] # 앞에서부터 M개만큼 빼고 나머지를 negative_data에 저장
else:
    if -negative_data[0] > positive_data[-1]: # 음수 쪽에 절대값의 최대가 있을 경우
        result += -negative_data[0]
        negative_data = negative_data[M:]
    else: # 양수 쪽에 절대값의 최대가 있을 경우
        result += positive_data[-1]
        positive_data = positive_data[:positive_len - M]
    
positive_data.sort(reverse = True) # 최대를 앞으로 오게 하기 위해 positive_data 내림차순 정렬

# index % M == 0 인 데이터들만 필요
# 어차피 나머지가 있는 데이터들의 경우 나머지가 없는 데이터가 가면서 다 정리
negative_result = [x for x in negative_data if negative_data.index(x) % M == 0] 
positive_result = [x for x in positive_data if positive_data.index(x) % M == 0]

# 계산
# 책 꽂으로 갔다가 다시 와야되니까 *2
result += 2 * sum(positive_result) - 2 * sum(negative_result)

print(result)