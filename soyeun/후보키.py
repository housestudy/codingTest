from itertools import combinations

def solution(relation):
    n = len(relation)
    m = len(relation[0])

    combi = []
    for i in range(1,m+1):
        combi.extend(combinations(range(m),i))

    unique = []
    for j in combi:
        temp = [tuple(item[key] for key in j) for item in relation]
        if len(set(temp)) == n:
            unique.append(j)

    answer = set(unique)
    for k in range(len(unique)):
        for l in range(k+1,len(unique)):
            if len(unique[k]) == len(set(unique[k]) & set(unique[l])):
                answer.discard(unique[l])

    return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))