import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {

        int sum = 0;
        int time = 0;
        Queue<Integer> bridge = new LinkedList<Integer>();
        Queue<Integer> out = new LinkedList<>();
        for(int i = 0; i< truck_weights.length; i++) {
            while (true) {
                if (bridge.isEmpty()) {
                    bridge.add(truck_weights[i]);
                    sum += truck_weights[i];
                    time++;
                    break;
                } else if (bridge.size() == bridge_length) {
                    sum -= bridge.poll();
                } else {
                    if (sum + truck_weights[i] <= weight) {
                        bridge.add(truck_weights[i]);
                        sum += truck_weights[i];
                        time++;
                        break;
                    } else {
                        bridge.add(0);
                        time++;
                    }
                }
            }
        }
        return time + bridge_length;
    }
}