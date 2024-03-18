// 240318 다단계 칫솔판매
// 트리

import java.util.*;

class Solution {
    Map<String, Integer> result = new HashMap<>();
    Map<String, String> refer = new HashMap<>();

    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {

        for (int i = 0; i < enroll.length; i++) {
            refer.put(enroll[i], referral[i]);
            result.put(enroll[i], 0);
        }

        for (int i = 0; i < seller.length; i++) {
            distribute(seller[i], amount[i]);
        }

        int[] answer = new int [enroll.length];

        for(int i = 0; i < enroll.length; i++) {
            answer[i] = result.get(enroll[i]);
        }

        return answer;
    }

    void distribute(String seller, int amount) {
        int now = amount * 100;

        while(true) {
            String upper = refer.get(seller);
            int upCost = (int) (now * 0.1);
            int mine = now - upCost;

            result.put(seller, result.get(seller) + mine);

            now = upCost;

            if (upper.equals("-") || upCost == 0) return;
            seller = upper;
        }
    }
}