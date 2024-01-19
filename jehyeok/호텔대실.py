# https://school.programmers.co.kr/learn/courses/30/lessons/155651
# Lv2

# 내 답
# 어디서 무한루프가 도는거지..? 왜 i 가 0에서 안바뀌지
book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]

def solution(book_time):
    answer = 0

    book_time = sorted(book_time)
    book_time = [[int(y.split(':')[0]) * 60 + int(y.split(':')[1]) for y in x] for x in book_time]

    i = 0
    bookTimeLen = len(book_time)
    visited = [0] * bookTimeLen

    while i < bookTimeLen:
        book = book_time[i]
        visited[i] = 1
        end = book[1]

        for j in range(i + 1, bookTimeLen):
            if book_time[j][0] >= end + 10:
                i = j
                break

            if j == bookTimeLen:
                answer += 1
                i = visited.index(0)

    return answer

print(solution(book_time))