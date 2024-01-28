# 구현 문제. 스택으로 해결 가능해 보였다

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    password = deque(list(input()))
    password.pop()
    # 처음에는 입력창 하나랑 password 있으면 될 것 같았는데, > 때문에 두개 필요했다.
    answerleft = []
    answerright = deque([])
    for i in range(len(password)):
        button = password.popleft()
        if button == "<":
            if answerleft :
                temp = answerleft.pop()
                answerright.appendleft(temp)
            else:
                continue
        elif button == ">" :
            if answerright :
                temp = answerright.popleft()
                answerleft.append(temp)
            else: continue
        elif button == "-" :
            if answerleft :
                answerleft.pop()
            else: continue
        else:
            answerleft.append(button)
    while answerright:
        answerleft.append(answerright.popleft())
    answer = ("").join(answerleft)
    print(answer)