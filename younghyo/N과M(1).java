// 백준 N과 M (1), 실버 3, https://www.acmicpc.net/problem/15649
// 백트래킹

import java.util.*;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;

public class BackTrack {

	public static boolean[] visit;
	public static int[] arr;
	public static int n, m;
	public static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		arr = new int[m];
		visit = new boolean[n + 1];

		dfs(0);
		System.out.println(sb);
	}

	public static void dfs(int cnt) {

		if (cnt == m) {
			for (int val : arr) {
				sb.append(val).append(" ");
			}
			sb.append("\n");
			return;
		}

		for (int i = 1; i <= n; i++) {
			if (!visit[i]) { 
				visit[i] = true; 
				arr[cnt] = i; 
				dfs(cnt + 1);
				visit[i] = false;
			}
		}
	}
}
