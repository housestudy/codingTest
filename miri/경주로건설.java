import java.util.*;
public class Solution {
    static int[][][] visited;
    static int N;
    static int[][] d = {{1,0},{-1,0},{0,-1},{0,1}};

    public int solution(int[][] board) {
        N = board.length;
        visited = new int[N][N][4];

        return bfs(board);
    }

    public class Node {
        int r, c, dir, cost;
        public Node(int r, int c, int dir, int cost) {
            this.r = r;
            this.c = c;
            this.dir = dir;
            this.cost = cost;
        }
    }

    public int bfs(int[][] board) {
        int x = 0, y = 0, direction = -1, cost = 0;
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(x,y,direction,cost));

        int min_cost = Integer.MAX_VALUE;

        while(!q.isEmpty()) {
            Node now = q.poll();

            if(now.r == N-1 && now.c == N-1) {
                min_cost = Math.min(min_cost, now.cost);
            }

            for(int dir = 0; dir < 4; dir++) {
                int dr = now.r + d[dir][0];
                int dc = now.c + d[dir][1];

                if(dr < 0 || dr >= N || dc < 0 || dc >= N || board[dr][dc] == 1){
                    continue;
                }

                int nextCost = now.cost;
                if(now.dir == -1 || now.dir == dir) {
                    nextCost += 100;
                } else {
                    nextCost += 600;
                }

                if(visited[dr][dc][dir] == 0 || board[dr][dc] >= nextCost) {
                    q.add(new Node(dr, dc, dir, nextCost));
                    visited[dr][dc][dir] = 1;
                    board[dr][dc] = nextCost;
                }
            }
        }
        return min_cost;
    }
}