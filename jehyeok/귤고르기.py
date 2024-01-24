k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

def solution(k, tangerine):
    answer = 0

    sizes = [0] * (max(tangerine) + 1)

    for i in tangerine:
        sizes[i] += 1

    sizes = sorted(sizes, reverse=True)

    for size in sizes:
        k -= size
        answer += 1

        if k <= 0:
            break

    return answer

print(solution(k, tangerine))