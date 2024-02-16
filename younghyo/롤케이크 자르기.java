// 프로그래머스 롤 케잌 자르기
// 정신차려

import java.util.HashMap;
import java.util.Map;

public class Main {
    public int solution(int[] topping) {
        int answer = 0;

        Map<Integer, Integer> chulsu = new HashMap<>();
        Map<Integer, Integer> brother = new HashMap<>();

        // for문 돌면서  토핑 개수 넣기
        for (int i = 0; i < topping.length; i++) {
            int t = topping[i];
            if (chulsu.containsKey(t)) {
                chulsu.put(t, chulsu.get(t) + 1);
            } else {
                chulsu.put(t, 1);
            }
        }

        for (int i = 0; i < topping.length; i++) {
            int t = topping[i];
            // 둘의 크기가 같다면
            if (brother.size() == chulsu.size()) {
                answer++;
            }
            // 동생 케이크에 없는 토핑을 토핑 추가
            if (!brother.containsKey(t)) {
                brother.put(t, 1);
            }
            // 형 토핑은 하나 빼주기
            chulsu.put(t, chulsu.get(t) - 1);
            // 만약 해당 토핑이 없으면 remove
            if (chulsu.get(t) == 0) {
                chulsu.remove(t);
            }
        }
        return answer;
    }
}