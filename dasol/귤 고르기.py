def solution(k, tangerine):
    counts = [0 for _ in range(10**7+1)]
    for tan in tangerine:
        counts[tan] += 1
    
    counts.sort(reverse= True)
    basket = 0
    size_type = 0
    for count in counts:
        if count >= k:
            return 1
        basket += count
        size_type += 1
        if basket >= k:
            return size_type