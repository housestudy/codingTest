import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Solution7 {
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        PriorityQueue<Integer> plusQ = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minusQ = new PriorityQueue<>(Comparator.reverseOrder());

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            int now = Integer.parseInt(st.nextToken());
            if(now >= 0){
                plusQ.add(now);
            } else {
                minusQ.add(Math.abs(now));
            }
        }

        int endPoint = 0;

        if(plusQ.isEmpty()) {
            endPoint = minusQ.peek();
        } else if(minusQ.isEmpty()) {
            endPoint = plusQ.peek();
        } else {
            endPoint = Math.max(minusQ.peek(), plusQ.peek());
        }


        int move = 0;
        while(!plusQ.isEmpty()){
            move += plusQ.peek()*2;
            for(int i=0; i<M; i++) plusQ.poll();
        }

        while(!minusQ.isEmpty()){
            move += minusQ.peek()*2;
            for(int i=0; i<M; i++) minusQ.poll();
        }

        move -= endPoint;
        System.out.println(move);
    }
}
