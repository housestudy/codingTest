import itertools
def cal(a,b,oper):
    if oper == '-':
        return a-b
    elif oper == '*':
        return a*b
    elif oper == '+':
        return a+b
def solution(expression):
    answer = 0
    operation = ['-','+','*']
    exp_oper = set()
    exp_list = []
    temp = ''
    for exp in expression:
        if exp in operation:
            exp_list.append(int(temp))
            exp_list.append(exp)
            exp_oper.add(exp)
            temp = ''
        else:
            temp += exp
    exp_list.append(int(temp))
    print(exp_list)
    perm = list(itertools.permutations(exp_oper))
    print(perm)
    for prior_per in perm:
        temp_exp_list = exp_list.copy()
        for target_oper in prior_per:
            stack = []
            temp_oper = ''
            for exp_val in temp_exp_list:
                if temp_oper == target_oper:
                    a = stack.pop()
                    b = exp_val
                    stack.append(cal(a, b, temp_oper))
                    temp_oper = ''
                elif exp_val == target_oper:
                    temp_oper = exp_val
                else:
                    stack.append(exp_val)
            temp_exp_list = stack.copy()
        answer = max(answer,abs(stack[0]))

    return answer