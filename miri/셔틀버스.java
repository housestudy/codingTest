import java.util.*;

public class Solution {
    public String solution(int n, int t, int m, String[] timetable) {
        int[] hours = new int[timetable.length];
        int[] minutes = new int[timetable.length];
        int[] timetables = new int[timetable.length];
        for(int i = 0; i < timetable.length; i++) {
            String[] parts = timetable[i].split(":");
            hours[i] = Integer.parseInt(parts[0]) * 60;
            minutes[i] = Integer.parseInt(parts[1]);
            timetables[i] = hours[i] + minutes[i];
        }
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int time : timetables) {
            queue.offer(time);
        }

        int start_time = 9 * 60;
        int last_time = 0;
        int total = 0;
        for(int i = 0; i < n; i++) {
            total = 0;
            while(!queue.isEmpty()) {
                int memtime = queue.peek();
                if(memtime <= start_time && total < m) {
                    queue.poll();
                    total++;
                } else {
                    break;
                }
                last_time = memtime - 1;
            }
            start_time += t;
        }
        if(total < m){
            last_time = start_time - t;
        }
        String hour = String.format("%02d", last_time / 60);
        String minute = String.format("%02d",last_time % 60);
        return hour + ":" + minute;
    }
}