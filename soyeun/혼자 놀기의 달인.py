from collections import Counter
def solution(cards):
    answer = 0
    n = len(cards)
    cards = [0] + cards
    parent = [num for num in range(n+1)]
    def get_parent(parent, x):
        if parent[x] == x:
            return x
        else:
            return get_parent(parent,parent[x])
    def union_parent(a,b,parent):
        a = get_parent(parent,parent[a])
        b = get_parent(parent,parent[b])

        if a > b:
            parent[a] = b
        else:
            parent[b] = a
        return parent
    def find_parent(a,b,parent):
        a = get_parent(parent, parent[a])
        b = get_parent(parent, parent[b])

        if a == b:
            return False
        else:
            return True

    for i in range(1,n+1):
        ch = i
        while find_parent(ch,cards[ch],parent):
            union_parent(ch, cards[ch], parent)
            ch = cards[ch]
    parent_dict = Counter(parent)

    if len(parent_dict) <= 2:
        return 0
    else:
        parent_list = sorted(parent_dict.items(), key = lambda x:(-x[1],x[0]),)
        answer = parent_list[0][1] * parent_list[1][1]
        return answer

cards = [8,6,3,7,2,5,1,4]
print(solution(cards))
