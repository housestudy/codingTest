// 미로 찾기 명령어
// DFS
// 바보

import java.util.ArrayList;
import java.util.List;

public class Solution {
    String command = "dlru";
    ArrayList<Integer> dx = new ArrayList<>(List.of(1, 0, 0, -1));
    ArrayList<Integer> dy = new ArrayList<>(List.of(0, -1, 1, 0));
}
    public static boolean OOB(int x, int y, int n, int m) {
        return x > 0 && x <= n && y > 0 && y <= m;
    }

    public static void dfs(int x, int y, ArrayList<Integer> info, Solution sol, StringBuilder answer, StringBuilder stack, int depth, boolean[] dfsExit) {
        if (dfsExit[0]) {
            return;
        }
        int n = info.get(0);
        int m = info.get(1);
        int r = info.get(2);
        int c = info.get(3);
        int k = info.get(4);

        if (k - depth < Math.abs(x - r) + Math.abs(y - c)) {
            return;
        }

        if (depth == k) {
            if (x == r && y == c) {
                answer.append(stack);
                dfsExit[0] = true;
            }
            return;
        }

        for (int d = 0; d < 4; d++) {
            int nextX = x + sol.dx.get(d);
            int nextY = y + sol.dy.get(d);
            if (OOB(nextX, nextY, n, m)) {
                stack.append(sol.command.charAt(d));
                dfs(nextX, nextY, info, sol, answer, stack, depth + 1, dfsExit);
                stack.deleteCharAt(stack.length() - 1);
            }
        }
    }

    public static String solution(int n, int m, int x, int y, int r, int c, int k) {
        StringBuilder answer = new StringBuilder();
        StringBuilder stack = new StringBuilder();
        ArrayList<Integer> info = new ArrayList<>(List.of(n, m, r, c, k));
        boolean[] dfsExit = {false};
        int remain = Math.abs(x - r) + Math.abs(y - c);
        if ((k - remain) % 2 != 0 || remain > k) {
            answer.append("impossible");
        } else {
            dfs(x, y, info, sol, answer, stack, 0, dfsExit);
        }
        return answer.toString();
    }


}