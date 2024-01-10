def solution(users, emoticons):
    # 모든 case를 전부 조사해서 그중에 제일 많은 걸로 가야하는 걸까? n-back 알고리즘을 쓰면 어떨까?
    length_user = len(users)
    length_emoticons = len(emoticons)
    tracking = [ 0 for _ in range(length_emoticons)]
    answer = [0, 0]

    def cal():
        cal_result = [0,0]
        for i in range(length_user):
            sum = 0 # 중간 합 for user 1명
            for j in range(length_emoticons):
                num = 0
                if tracking[j] == 0:
                    num = 0.4
                elif tracking[j] == 1:
                    num = 0.3
                elif tracking[j] == 2:
                    num = 0.2
                else:
                    num = 0.1
                if num*100 >= users[i][0] :
                    sum += emoticons[j]*(1 - num)
            if sum >= users[i][1]:
                cal_result[0] += 1
            else:
                cal_result[1] += sum
        return cal_result
    
    def nback(n, totaldepth):
        
        for i in range(4):
            tracking[n] = i
            if n != totaldepth-1:
                nback(n+1, totaldepth)
            result = cal()
            if result[0] > answer[0] :
                answer[0], answer[1] = result[0], result[1]
            elif result[0] == answer[0] :
                    if result[1] > answer[1]:
                        answer[1] = result[1]
        
        return
    
    nback(0, length_emoticons)
    answer[1] = int(answer[1])
    return answer



test1_user, test1_emoticons = [[40, 10000], [25, 10000]], [7000, 9000]
test2_user, test2_emoticons = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]

print(solution(test2_user, test2_emoticons))