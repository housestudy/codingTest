# 비슷한 단어
# 1. 같은 구성(같은 종류의 문자, 같은 개수)
# 2. 기존에 있는 문자에서 한 단어를 추가하거나 빼기(1개 차이) - 하나 빼고 다 똑같아야 함
# GOD GODT  GOD GGGG
# 3. 하나의 문자를 다른 문자로 바꿈(문자의 종류 개수가 1개 차이)
# 풀이
# 1. 비슷한 단어 조건을 하나씩 확인하면 될 듯
# 2. 같은 구성(단어 길이가 같고 문자의 종류도 같음)
# 3. 기존에 있는 문자에서 한 단어를 추가하거나 빼기(단어 길이 차이가 1개 날 경우)
# 3-1) 단어에 있는 문자의 종류가 같을 때
# 3-2) 단어에 있는 문자의 종류가 1개 차이
# 4. 하나의 문자를 다른 문자로 바꿈(단어의 길이 같음)
# 4-1) 단어에 있는 문자의 종류가 1개 차이


answer = 0
n = int(input())
first = list(input())

for i in range(n-1):
    temp = first[:]
    word = list(input())
    cnt = 0

    for w in word:
        if w in temp:
            temp.remove(w)
        else:
            cnt += 1

    if len(temp) <= 1 and cnt <= 1:
        answer += 1

print(answer)

