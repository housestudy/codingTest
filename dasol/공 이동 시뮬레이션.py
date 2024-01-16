# 단순 구현 문제로 접근했지만, 어림도 없었고~
# 역으로 해결하기. 그리고 공의 이동에 집중하면 문제에 빠진다. 공의 이동이 아니라 영역의 이동으로 보면 문제가 더 단순해진다.

def solution(n, m, x, y, queries):
    answer = 0
    x_min, x_max, y_min, y_max = x, x, y, y

    for idx in range(len(queries) - 1, -1, -1):
        direc, dist = queries[idx]
        if direc == 0:  # 좌(오른쪽에서 왔음)
            y_max += dist  # 오른쪽으로 늘리기
            if y_max > m - 1: # 범위 벗어나면
                y_max = m - 1  # 끝값으로
            if y_min != 0:  # 왼쪽 값이 끝이 아니면 범위 축소
                y_min += dist

        elif direc == 1:  # 우(왼쪽에서 왔음)
            y_min -= dist
            if y_min < 0:
                y_min = 0
            if y_max != m - 1:
                y_max -= dist

        elif direc == 2:  # 상(아래서 왔음)
            x_max += dist
            if x_max > n - 1:
                x_max = n - 1
            if x_min != 0:
                x_min += dist

        else:  # 하(위에서 왔음)
            x_min -= dist
            if x_min < 0:
                x_min = 0
            if x_max != n - 1:
                x_max -= dist
        if y_min > m - 1 or y_max < 0 or x_min > n - 1 or x_max < 0:
            return answer
    else:
         answer = (y_max - y_min + 1) * (x_max - x_min + 1)
    return answer