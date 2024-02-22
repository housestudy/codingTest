import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    commands = list(input().strip())
    N = int(input())
    datas = input().strip()

    datas = datas.strip('[')
    datas = datas.strip(']')
    
    queue = deque(datas.split(','))

    printErr = False
    reverseFlag = False

    for command in commands:
        if command == 'R':
            reverseFlag = not reverseFlag
        else:
            if N == 0:
                printErr = True
                break
            else:
                if reverseFlag:
                    queue.pop()
                else:
                    queue.popleft()

                N -= 1

    if reverseFlag:
        queue.reverse()
        
    if printErr:
        print('error')
    else:
        printData = ','.join(queue)
        print('[' + printData + ']')