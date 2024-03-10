// 표 편집

import java.util.*;
class Solution {
    private static int move(int num,int now,int[] arr){
        for(int i = 0 ; i < num ; i++){

            now = arr[now];
        }
        return now;
    }
    private static int doCmd(int now,
                             boolean[] isValid,
                             int[] prev,
                             int[]next,
                             String cmd,
                             ArrayDeque<Integer>stack){
        if("C".equals(cmd)){
            stack.push(now);
            isValid[now] = false;
            int prevIndex = move(1,now,prev);
            int nextIndex = move(1,now,next);
            if(prevIndex != -1){
                next[prevIndex] = nextIndex;
            }
            if(nextIndex != -1){
                prev[nextIndex] = prevIndex;
            }
            if(nextIndex != -1){
                now = nextIndex;
            }else{
                now = prevIndex;
            }
            return now;
        }
        if("Z".equals(cmd)){
            int index = stack.poll();
            isValid[index] = true;
            int prevIndex = move(1,index,prev);
            int nextIndex = move(1,index,next);
            if(prevIndex != -1){
                next[prevIndex] = index;
            }
            if(nextIndex != -1){
                prev[nextIndex] = index;
            }
            return now;
        }
        String[] temp = cmd.split(" ");
        int num = Integer.parseInt(temp[1]);
        if("D".equals(temp[0])){
            now = move(num,now,next);
            return now;
        }
        if("U".equals(temp[0])){
            now = move(num,now,prev);
            return now;
        }
        System.out.println("???");
        return -1;
    }
    public String solution(int n, int k, String[] cmds) {
        String answer = "";
        int[] prev = new int[n];
        int[] next = new int[n];
        boolean[] isValid = new boolean[n];
        Arrays.fill(isValid,true);
        for(int i = 0 ; i < n ; i++){
            prev[i] = i-1;
            next[i] = i+1;
        }
        next[n-1] = -1;
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        int now = k;
        for(String cmd : cmds){
            now = doCmd(now,isValid,prev,next,cmd,stack);
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0 ; i < n ; i++){
            if(isValid[i]){
                sb.append("O");
            }else{
                sb.append("X");
            }
        }
        answer = sb.toString();
        return answer;
    }
}

