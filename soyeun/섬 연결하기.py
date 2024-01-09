def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    def get_parent(parent, x):
        if parent[x] == x:
            return x
        return get_parent(parent, parent[x])

    def union_parent(parent, a, b):
        a = get_parent(parent, a)
        b = get_parent(parent, b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def find_parent(parent, a, b):
        a = get_parent(parent, a)
        b = get_parent(parent, b)

        if a == b:
            return True
        else:
            return False

    for a, b, cost in costs:
        if find_parent(parent, a, b) == False:
            union_parent(parent, a, b)
            answer += cost

    return answer