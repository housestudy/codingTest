
// 각 큐의 합
// 큐ㅠ...

import java.util.*;
class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;

        int n = queue1.length;

        long[] merge = new long[n * 2]; // 하나의 배열로 합치

        for (int i = 0; i < n; i++) {
            merge[i] = queue1[i];
        }

        for (int i = 0; i < n; i++) {
            merge[n + i] = queue2[i];
        }

        long q1Sum = Arrays.stream(queue1).sum();
        long q2Sum = Arrays.stream(queue2).sum();


        if ((q1Sum + q2Sum) % 2 != 0) {
            return -1;
        }

        long result = (q1Sum + q2Sum) / 2;

        Arrays.sort(queue1);
        Arrays.sort(queue2);

        int i = 0, j = 0;

        while (i < n && j < n) {
            if (q1Sum + queue1[i] <= result) {
                q1Sum += queue1[i++];
            } else {
                q2Sum += queue1[i++] - result +  q2Sum;
                answer++;
            }

            if (q2Sum + queue2[j] <= result) {
                q2Sum += queue2[j++];
            } else {
                q1Sum  += queue2[j++] - result + q1Sum ;
                answer++;
            }
        }

        return answer;
    }

}