import java.util.*;

class Solution {
    public int Solution(int k, int[] tangerine) {
        int sum = 0; //귤의 개수
        int cnt = 0; //귤 크기 최솟값

        Map<Integer,Integer> map = new HashMap<>();
        for (int i : tangerine) {
            map.put(i,map.getOrDefault(i,0)+1);
        }

        //개수가 많은 귤 크기순으로 배열
        ArrayList<Integer> list = new ArrayList<>(map.values());
        Collections.sort(list,Collections.reverseOrder());

        for (Integer i : list) {
            if(sum + i >= k) {
                cnt++;
                break;
            } else {
                sum += i;
                cnt++;
            }
        }
        return cnt;
    }
}