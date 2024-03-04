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

# 답
def solution(n, m, x, y, r, c, k):
    counts = {'d': 0, 'l': 0, 'r': 0, 'u': 0}
    extra = '' # 3번에 해당
    
    x_diff, y_diff = r - x, c - y
    x_direction = 'u' if x_diff < 0 else 'd' # 탈출 지점의 방향
    y_direction = 'l' if y_diff < 0 else 'r' # 탈출 지점의 방향
    
    # 아래, 왼쪽 벽과의 거리
    x_wall, y_wall = min(n - x, n - r), min(y, c) - 1 
    
    # 맨해튼 거리를 초과하는 이동 수
    extra_moves = k - (abs(x_diff) + abs(y_diff))

    if extra_moves < 0 or extra_moves % 2 == 1:
        return 'impossible'
    
    # 탈출 지점까지 이동
    counts[x_direction] += abs(x_diff)
    counts[y_direction] += abs(y_diff)

	# 1번 & 5번
    if extra_moves > x_wall * 2: # 여유가 있다면 벽을 찍고 돌아오고
        counts['d'] += x_wall
        counts['u'] += x_wall
        extra_moves -= x_wall * 2
    else:						# 아니라면 가능한 만큼만 아래로 다녀온다
        counts['d'] += extra_moves // 2
        counts['u'] += extra_moves // 2
        extra_moves = 0
    
    # 2번 & 4번
    if extra_moves > y_wall * 2: # 여유가 있다면 벽을 찍고 돌아오고
        counts['l'] += y_wall
        counts['r'] += y_wall
        extra_moves -= y_wall * 2
    else:						# 아니라면 가능한 만큼 왼쪽으로 다녀온다
        counts['l'] += extra_moves // 2
        counts['r'] += extra_moves // 2
        extra_moves = 0

	# 3번
    if extra_moves > 0: # 그래도 여유가 있으면 rl 와리가리
        extra = 'rl' * (extra_moves // 2)

	# 빠른 순서대로 합친다
    answer = counts['d'] * 'd' + counts['l'] * 'l' + extra + counts['r'] * 'r' + counts['u'] * 'u'
    return answer