def solution(cap, n, deliveries, pickups):
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        have_to_deli += deliveries[n - i - 1]
        have_to_pick += pickups[n - i - 1]

        # deliveries와 pickups의 구성요소가 음수가되면 안된다고 생각했는데, 어차피 위에서 더해주기 때문에 상관 없어진다.
        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n-i) * 2

    return answer