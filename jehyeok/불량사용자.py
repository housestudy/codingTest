from itertools import permutations

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

def funcIsSame(user, ban):
    if len(user) != len(ban):
        return False
    
    for a, b in zip(user, ban):
        if b == '*': continue
        if a != b: return False
        
    return True

def solution(user_id, banned_id):
    answer = 1
    result = []

    for data in permutations(user_id, len(banned_id)):
        flag = 0
        for a, b in zip(data, banned_id):
            if funcIsSame(a, b):
                flag += 1

        if flag == len(banned_id):
            if set(data) not in result:
                result.append(set(data))

    answer = len(result)

    return answer

print(solution(user_id, banned_id))