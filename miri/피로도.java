class Solution {
    public int max;

    public int solution(int k, int[][] dungeons) {
        int[] visited = new int[dungeons.length];
        explore(dungeons, visited, k, 0);

        return max;
    }

    public void explore(int[][] dungeons, int[] visited, int k, int cnt) {
        for(int i = 0; i < dungeons.length; i++) {
            if(visited[i] == 0 && k >= dungeons[i][0]){
                visited[i] = 1;
                explore(dungeons,visited,k-dungeons[i][1],cnt+1);
                visited[i] = 0;
            }
        }

        if(max < cnt) {
            max = cnt;
        }
    }
}