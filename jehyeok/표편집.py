n, k = 8, 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

def solution(n, k, cmd):
    answer = ''
    arr = [x for x in range(n)]
    deleted = []
    
    for data in cmd:
        command = data[0]
        number = '0'

        if len(data) > 1:
            number = data[-1]

        if command == 'U':
            deletedNum = len([x for x in deleted if x < k])
            k -= (int(number) + deletedNum)

        if command == 'D':
            deletedNum = len([x for x in deleted if x > k])
            k += (int(number) + deletedNum)

        if command == 'C':
            arr[k] = -1
            deleted.append(k)

            if k == n - 1: k -= 1
            else: k += 1

        if command == 'Z':
            v = deleted.pop()
            arr[v] = v

            if v != n - 1: k += 1

    for i in arr:
        if i == -1:
            answer += 'X'
        else:
            answer += 'O'

    return answer

print(solution(n, k, cmd))