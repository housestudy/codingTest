import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long sum1 = 0;
        long sum2 = 0;
        Queue<Integer> qq1 = new LinkedList<Integer>();
        Queue<Integer> qq2 = new LinkedList<Integer>();
        for(int i = 0; i < queue1.length; i++) {
            sum1 += queue1[i];
            sum2+= queue2[i];
            qq1.add(queue1[i]);
            qq2.add(queue2[i]);
        }
        long total = sum1 + sum2;
        if(total % 2 == 1) {
            return -1;
        }

        while(true) {
            if(answer>(queue1.length+queue2.length)*2) return -1;
            if(sum1==total/2) break;
            else if(sum1>total/2) {
                sum1-=qq1.peek();
                qq2.add(qq1.poll());
            }else {
                sum1 += qq2.peek();
                qq1.add(qq2.poll());
            }
            answer++;
        }


        return answer;
    }
}