from collections import deque
import itertools

def solution(expression):
    equation = list(expression)
    numbers = []
    temp = []
    def flush ():
        numbers.append(int(''.join(temp)))
        temp.clear()

    for x in equation :
        if x == "*":
            flush()
            numbers.append(x)
        elif x == "+":
            flush()
            numbers.append(x)
        elif x == "-":
            flush()
            numbers.append(x)
        else:
            temp.append(x)
    flush()
    cal = ['+', '-', "*"]
    priorities = list(itertools.permutations(cal))
    answers = []
    calculator =[]
    calculator.append(numbers)
    for _ in range(3):
        calculator.append([])
    # print(calculator)

    for prio in priorities:
        for i in range(3):
            flag = False
            for j in range(len(calculator[i])) :
                x = calculator[i][j]
                if flag :
                    flag = False
                    continue
                if x == prio[i]:
                    flag = True
                    y = calculator[i+1].pop()
                    if prio[i] == "*":
                        calculator[i+1].append(y * calculator[i][j+1])
                    elif prio[i] == "+":
                        calculator[i+1].append(y + calculator[i][j+1])
                    else:
                        calculator[i+1].append(y - calculator[i][j+1])
                else:
                    calculator[i+1].append(x)
            
        answers.append(abs(calculator[3][0]))
        for k in range(3):
            calculator[k+1] = []
    
    return max(answers)



test1 = "100-200*300-500+20"
test2 = "50*6-3*2"

print(solution(test2))