def solution(book_time):
    times = [0 for _ in range(60*24+11)]
    answer = 0
    for s , e in book_time:
        s_h, s_m = map(int ,s.split(':'))
        e_h, e_m = map(int ,e.split(':'))
        for i in range(s_h*60 + s_m, e_h*60 + e_m+10):
            times[i] += 1
    answer = max(times)
    return answer