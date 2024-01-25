#  내가 푼 풀이 = 정석 풀이
#  노드의 부모 설정이 완벽하게 설정되지 않아서, 실제로 그룹을 찾을 때 문제
#  그냥 무식하게 전부 get_parent() 함수 돌려서 찾았다.
def solution(n, wires):
    wires.sort(key = lambda x : (x[0], x[1]))
    def get_parent(grid_map, x):
        if grid_map[x] == x:
            return x
        else:
            real_parent = get_parent(grid_map, grid_map[x])
            grid_map[x] = real_parent
            return real_parent
        

    def set_connec(small, big, grid_map):
        small = get_parent(grid_map, small)
        big = get_parent(grid_map, big)
        if small < big :
            grid_map[big] = small
        else:
            grid_map[small] = big

    
    count = []
    for idx in range(n-1): # 몇번 째 다리를 끊을건지
        union_map = [i for i in range(n+1)]
        # 커넥션 설정
        for j in range(idx):
            set_connec(wires[j][0], wires[j][1], union_map)
        for j in range(idx+1, n-1):
            set_connec(wires[j][0], wires[j][1], union_map)

        first_group = get_parent(union_map, n)
        left = 0
        right = 1
        for j in range(1, n): # 양 쪽이 몇 개인지.
            if get_parent(union_map, n-j)!= first_group :
                left += 1
            else:
                right += 1
        count.append([left, right])

    answer = n+1
    for i in range(len(count)):
        answer = min(answer, abs(count[i][0] - count[i][1]))
    return answer


# 전부 시간이 0.5ms 안으로 나오는 기적의 코드
# 질문하기 들어갔다가 우연히 발견
#  딕셔너리 활용해서 하는 것 같은데, 어떻게 하는지는 여전히 이해 안됨 너무 졸림
#  자러감. ㅅㄱ

from collections import deque, defaultdict

def solution(n, wires):
    wires = [[i-1, j-1] for i, j in wires]
    routes = [[] for _ in range(n)]
    vals = [defaultdict(int) for _ in range(n)]
    for i, j in wires:
        routes[i].append(j)
        routes[j].append(i)
    tovisit = deque(range(n))
    minv = n
    while len(tovisit) > 1:
        tovisit.rotate()
        cn = tovisit[-1]
        if len(routes[cn]) == len(vals[cn])+1:
            tovisit.pop()
            v = 1
            for i in routes[cn]:
                if not vals[cn][i]:
                    nn = i
                v += vals[cn][i]
            vals[nn][cn] = v
            minv = min(minv, abs(n-2*v))
    return minv