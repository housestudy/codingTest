import sys

input = sys.stdin.readline

letters = list(input().rstrip())

letters2 = []

M = int(input())

for i in range(M):
    comm = list(input().split())
    if len(comm) == 1:
        if comm[0] == "L":
            if letters:
                letters2.append(letters.pop())
        elif comm[0] == "D":
            if letters2:
                letters.append(letters2.pop())
        else:
            if letters:
                letters.pop()
    else:
        letters.append(comm[1])

letters2 = reversed(letters2)
ans = ("").join(letters) + ("").join(letters2)

print(ans)
