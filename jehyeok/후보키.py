relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	

# from itertools import combinations

# def solution(relation):
#     answer = []
#     results = []

#     rowLen = len(relation)
#     colLen = len(relation[0])
#     cols = [x for x in range(0, colLen)]

#     for i in range(1, colLen + 1):
#         for col in combinations(cols, i):
#             arr = []

#             for data in relation:
#                 tmp = []

#                 for k in col:
#                     tmp.append(data[k])

#                 arr.append(tmp)

#             arr = list(set([tuple(set(item)) for item in arr]))
#             if len(arr) == rowLen:
#                 results.append(col)

#     # results[i] == 뒤에서부터 세는놈
#     for i in range(len(results) - 1, 0, -1):
#         # results[j] == 앞에서부터 비교하는 놈
#         for j in range(0, i):
#             flag = True

#             for k in range(1, len(results[j]) + 1):
#                 for data in combinations(list(results[j]), k):
#                     print(results[i], j, results[j], data)
#                     # results[i]가 results[j]로 만들 수 있는 모든 조합 중 하나에 포함된다면 중복이므로..
#                     # ㅎ 못하겠다 ㅅㅂ
#                     if data in results[i]:
#                         flag = False
#                         break
            
#             if flag:
#                 answer.append(results[i])

#     return len(answer)

# print(solution(relation))

# 답
# 뭔 모르는 파이썬 함수가 이렇게 많냐...
from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    #가능한 속성의 모든 인덱스 조합 
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
            
    #유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:    # 유일성
            put = True
            
            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break
                    
            if put: unique.append(i)
   
    return len(unique)

print(solution(relation))