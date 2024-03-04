n, m, x, y, r, c, k = 3, 4, 2, 3, 3, 1, 5

# 아 몰라
# d l r u
def solution(n, m, x, y, r, c, k):
    answer = ''
    cnt = 0
    
    # 일단 거리는 상관없이 Endpoint로 이동을 시켜놓고 사전순으로
    while x < r:
        answer += 'd'
        x += 1
        cnt += 1
    
    while y > c:
        answer += 'l'
        y -= 1
        cnt += 1

    while y < c:
        answer += 'r'
        y += 1
        cnt += 1

    while x > r:
        answer += 'u'
        x -= 1
        cnt += 1

    # 추가로 이동해야 하는 거리 확인하고
    dist = k - cnt

    # 만약 추가로 이동해야되는 거리가 음수면 애초에 못 가는 경우
    if dist < 0:
        answer = 'impossible'
    # 추가로 이동해야 하는 거리가 있으면 왔다갔다
    elif dist > 0:
        # 짝수여야 왔다갔다가 되는거고
        if dist % 2 == 0:
            half = dist // 2
            # Endpoint에 아래 공간이 남았으면
            if n - r >= 1:
                if half >= n - r:
                    for _ in range(n - r):
                        answer += 'd'
                    for _ in range(n - r):
                        answer += 'u'

                    half -= (n - r)
                else:
                    for _ in range(half):
                        answer += 'd'
                    for _ in range(half):
                        answer += 'u'

                    half = 0
            # Endpoint에 왼쪽 공간이 남았으면
            elif half > 0 and c - 1 >= 1:
                if half >= c - 1:
                    for _ in range(c - 1):
                        answer += 'l'
                    for _ in range(c - 1):
                        answer += 'r'

                    half -= (c - 1)
                else:
                    for _ in range(half):
                        answer += 'l'
                    for _ in range(half):
                        answer += 'r'

                    half = 0
            # Endpoint에 오른쪽 공간이 남았으면
            elif half > 0 and m - c >= 1:
                if half >= m - c:
                    for _ in range(m - c):
                        answer += 'r'
                    for _ in range(m - c):
                        answer += 'l'
                    
                    half -= (m - c)
                else:
                    for _ in range(half):
                        answer += 'r'
                    for _ in range(half):
                        answer += 'l'

                    half = 0
            # Endpoint에 위쪽 공간이 남았으면
            elif half > 0 and r - 1 >= 1:
                if half >= r - 1:
                    for _ in range(half):
                        answer += 'u'
                    for _ in range(half):
                        answer += 'd'
                    
                    half -= (r - 1)
                else:
                    for _ in range(half):
                        answer += 'u'
                    for _ in range(half):
                        answer += 'd'
                    
                    half = 0
            # 남은 공간 없으면 impossible
            else:
                answer = 'impossible'

            # 다 돌렸는데 half가 남았다면?
            # 여기만 하면 맞겠는데..?
            if half > 0:
                for _ in range(half):
                    answer += 'rl'
        # 홀수면 갔다가 다시 올수가 없으니 impossible
        else:
            answer = 'impossible'

    return answer

print(solution(n, m, x, y, r, c, k))