// [프로그래머스] 메뉴 리뉴얼
// 조합...

import java.util.*;

class Solution {
    static HashMap<String, Integer> hm;
    public String[] solution(String[] orders, int[] course) {
        hm = new HashMap<>();

        for(String o: orders) {
            char[] order = o.toCharArray();
            Arrays.sort(order);
            for (int j : course) {
                combination(0, 0, j, order, "");
            }
        }

        int[] maxCntOfCourse = new int[course[course.length -1] +1];
        for(String key: hm.keySet()) {

            if(hm.get(key) >= 2) {
                maxCntOfCourse[key.length()] = Math.max(hm.get(key), maxCntOfCourse[key.length()]);
            }
        }

        List<String> answerTemp = new ArrayList<>();

        for(String key: hm.keySet()) {
            for(int i=0; i< maxCntOfCourse.length; i++) {
                if(maxCntOfCourse[i] == 0) continue;
                if(key.length() == i && hm.get(key) == maxCntOfCourse[i]) {
                    answerTemp.add(key);
                }
            }
        }

        Collections.sort(answerTemp);
        String[] answer = new String[answerTemp.size()];
        int i=0;
        for(String str: answerTemp) {
            answer[i++] = str;
        }

        return answer;
    }

    private static void combination(int cnt, int start, int limit, char[] order, String result) {
        if(cnt == limit) {
            hm.put(result, hm.getOrDefault(result, 0)+1);
            return;
        }

        for(int i=start; i< order.length;i++) {
            combination(cnt+1, i+1, limit, order, result+order[i]);
        }
    }
}