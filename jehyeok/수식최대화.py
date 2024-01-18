from itertools import permutations

expression = "100-200*300-500+20"

# def solution(expression):
#     answer = 0

#     results = []

#     tmp_expression = expression
#     tmp_expression = tmp_expression.replace('*', '+').replace('-', '+')

#     nums = tmp_expression.split('+')

#     symbols = []
#     for x in expression:
#         if x == '+' or x == '-' or x == '*':
#             symbols.append(x)

#     symbols = list(set(symbols))

#     for symbol in permutations(symbols, len(symbols)):
#         new_str = ''

#         for j in range(len(symbols)):
#             new_str += (nums[j] + symbol[j])

#         new_str += nums[-1]
#         results.append(abs(eval(new_str)))

#     answer = max(results)

#     return answer

def solution(expression):
    answer = []

    tmp_expression = expression
    tmp_expression = tmp_expression.replace('*', '+').replace('-', '+')

    nums = tmp_expression.split('+')

    symbols = []
    for x in expression:
        if x == '+' or x == '-' or x == '*':
            symbols.append(x)

    expressions = []

    for j in range(len(symbols)):
        expressions.append(nums[j])
        expressions.append(symbols[j])

    expressions.append(nums[-1])

    for operators in list(permutations(['+', '-', '*'], 3)):
        tmp_expressions = expressions
        result = ''

        for operator in operators:
            i = 0

            while True:
                if i >= len(tmp_expressions) - 1:
                    break
                if tmp_expressions[i + 1] == operator:
                    result += (str(eval(tmp_expressions[i] + tmp_expressions[i + 1] + tmp_expressions[i + 2])))
                    i += 3
                else:
                    result += tmp_expressions[i]                

        answer.append(abs(eval(result)))

    return max(answer)


print(solution(expression))