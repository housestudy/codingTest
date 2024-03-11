// 무인도 여행
// BFS

import java.util.*;

class Solution {
    public int[] solution(String[] maps) {
        int n = maps.length;
        int m = maps[0].length();

        String[][] map = new String[n][m];

        for(int i = 0; i< maps.length; i++) {
            String s = maps[i];
            map[i] = s.split("");
        }

        List<Integer> answer = new ArrayList<Integer>();
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];
        int[] di = {1, -1, 0, 0};
        int[] dj = {0, 0, 1, -1};

        for(int i = 0; i<n; i++) {
            for(int j = 0; j<m; j++) {
                int count = 0;
                if ( !visited[i][j] && !"X".equals(map[i][j])) {
                    queue.add(new int[]{i, j});
                    visited[i][j] = true;
                    count += Integer.parseInt(map[i][j]);
                }

                // 인접 무인도 탐색
                while(!queue.isEmpty()) {
                    int[] tmp = queue.poll();

                    for(int k = 0; k<4; k++) {
                        int next_i = di[k] + tmp[0];
                        int next_j = dj[k] + tmp[1];

                        // 상하좌우 및 방문 확인 후 탐색
                        if (next_i >= 0 && next_i < n && next_j >=0 && next_j < m && !visited[next_i][next_j] && !"X".equals(map[next_i][next_j])) {
                            queue.add(new int[]{next_i, next_j});
                            visited[next_i][next_j] = true;
                            count += Integer.parseInt(map[next_i][next_j]);
                        }
                    }
                }

                if (count > 0) {
                    answer.add(count);
                }
            }
        }

        Collections.sort(answer);
        if (answer.isEmpty()) {
            answer.add(-1);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
