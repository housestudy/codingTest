

def solution(n, k, cmd):
    linked_list = {i:[i-1,i+1] for i in range(n)}
    answer = ['O']*n
    cancel_list = []
    for c in cmd:
        c = c.split()

        if c[0] == 'D':
            for _ in range(int(c[1])):
                k = linked_list[k][1]

        elif c[0] == 'U':
            for _ in range(int(c[1])):
                k = linked_list[k][0]

        elif c[0] == 'C':
            prev, nxt = linked_list[k]
            answer[k] = 'X'
            cancel_list.append((prev,k,nxt))

            if nxt == n:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == -1:
                linked_list[nxt][0] = prev
            elif nxt == n:
                linked_list[prev][1] = nxt
            else:
                linked_list[prev][1] = nxt
                linked_list[nxt][0] = prev

        else:
            prev, now, nxt = cancel_list.pop()
            answer[now] = 'O'

            if prev == -1:
                linked_list[nxt][0] = now
            elif nxt == n:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[nxt][0] = now
    return ''.join(answer)

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k, cmd))