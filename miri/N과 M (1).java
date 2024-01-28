import java.util.*;
import java.io.*;

pulic class Main {
    public static int[] arr;
    public static boolean[] visited;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        arr = new int[M];
        visited = new boolean[N];
        dfs(N, M, 0);
        System.out.println(sb);
    }

    public static void dfs (int N, int M, int depth) {
        if( M == depth ) {
            for (int i : arr) {
                sb.append(i).append(' ');
            }
            sb.append('\n');
            return;
        }

        for(int i = 0; i < N; i++) {
            if(!visited[i]) {
                visited[i] = true;
                arr[depth] = i + 1;
                dfs(N,M,depth + 1);
                visited[i] = false;
            }
        }
    }
}