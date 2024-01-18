from collections import deque


def rotations(s):
    queue = deque(list(s))
    num = queue.popleft()
    queue.append(num)
    return ''.join(list(queue))


def check_correct(s):
    stack = []
    for j in s:
        if len(stack) == 0:
            if j in [")", '}', ']']:
                return False
            else:
                stack.append(j)
        elif j == '}' and stack[-1] == '{':
            stack.pop()
        elif j == ')' and stack[-1] == '(':
            stack.pop()
        elif j == ']' and stack[-1] == '[':
            stack.pop()
        else:
            stack.append(j)
    if len(stack) == 0:
        return True
    else:
        return False


def solution(s):
    answer = 0
    n = len(s)

    for i in range(n):
        if check_correct(s):
            answer += 1
        s = rotations(s)

    return answer

