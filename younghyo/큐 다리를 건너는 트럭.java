//


import java.util.*;

class Solution {

    public int solution(int bridge_length, int weight, int[] truck_weights) {
        List<int[]> queue = new LinkedList<int[]>();
        int answer = 0;

        int i = 0;
        int totalWeight = 0;
        while (true) {

            for (int j = 0; j < queue.size();) {

                if (--queue.get(j)[1] == 0) {
                    totalWeight -= queue.get(j)[0];
                    queue.remove(j);
                } else {
                    j++;
                }
            }

            if (i < truck_weights.length && truck_weights[i] + totalWeight <= weight) {
                totalWeight += truck_weights[i];
                queue.add(new int[] { truck_weights[i++], bridge_length });
            }

            answer += 1;

            if (queue.size() == 0) {
                break;
            }

        }

        return answer;
    }
}