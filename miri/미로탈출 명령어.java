public class Solution {
    int[][] array;
    StringBuilder route;
    String answer = null;
    int endRow,endCol;
    int arrRow,arrCol;
    char[] dir = {'d','l','r','u'};
    int[] rdir = {1, 0, 0, -1};
    int[] cdir = {0, -1, 1, 0};

    private int distance(int x, int y, int r, int c) {
        return (int)Math.abs(x-r) + (int)Math.abs(y-c);
    }

    private void dfs(int r, int c, int depth, int k) {
        if(answer != null) {
            return;
        }
        if(depth + distance(r, c, endRow, endCol) > k) {
            return;
        }
        if(k == depth) {
            answer = route.toString();
            return;
        }
        for(int i=0; i<4; i++){

            int nextRow = r + rdir[i];
            int nextCol = c + cdir[i];
            if(nextRow <= arrRow && nextCol <= arrCol && nextRow > 0 && nextCol >0){
                route.append(dir[i]);
                dfs(nextRow, nextCol, depth+1, k);
                route.delete(depth, depth+1);
            }

        }
    }

    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        route = new StringBuilder();
        array = new int[n][m];
        endRow = r;
        endCol = c;
        arrRow = n;
        arrCol = m;
        int length = distance(x,y,r,c);
        if((k - length) % 2 == 1 || k < length) {
            return "impossible";
        }
        dfs(x, y, 0, k);
        return answer == null ? "impossible" : answer;
    }
}
