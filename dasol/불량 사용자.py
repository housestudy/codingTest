# def has_duplicates2(seq):
#     seen = []
#     unique_list = [x for x in seq if x not in seen and not seen.append(x)]
#     return unique_list


# def solution(user_id, banned_id):
#     combis = []
#     banlists = [0 for _ in range(len(banned_id))]

#     result = has_duplicates2(banned_id)

#     for ban in banned_id:
#         banchr = list(ban)
#         ban_num = 0
    
#         for user in user_id:
#             userchr = list(user)
#             if len(banchr) == len(userchr):
#                 flag = True
#                 for i in range(len(banchr)):
#                     if banchr[i] == "*":
#                         continue
#                     else:
#                         if banchr[i] != userchr[i]:
#                             flag = False
#                             break
#                 if flag :
#                    ban_num += 1
#         if ban in result:
#             tar = 0
#         else:
#             tar = 1
#         combis.append([ban_num,tar])

#     if not combis :
#         return 0
#     else:
#         answer = 1
#         for combi in combis:
#             answer *= combi
#         return answer

from itertools import permutations

# check 하는 건 동일하게 짰는데 permutation을 쓰는 이유를 난 전혀...모르겠네?
def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    ban_set = []

    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in ban_set:
                ban_set.append(users)

    return len(ban_set)