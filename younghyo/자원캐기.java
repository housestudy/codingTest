package codingTest;

// 백준,자원캐기
// DP

import java.util.*;

public class Mine {

	public static void main(String[] args) {

		Scanner scn = new Scanner(System.in);

		int[][] arr = new int[300][300];
		int[][] dp = new int[300][300];

		int N = scn.nextInt();
		int M = scn.nextInt();

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				arr[i][j] = scn.nextInt();
			}
		}

		dp[0][0] = arr[0][0];

		for (int i = 1; i < N; i++) {
			dp[i][0] = dp[i - 1][0] + arr[i][0];
		}

		for (int j = 1; j < M; j++) {
			dp[0][j] = dp[0][j - 1] + arr[0][j];
		}

		for (int i = 1; i < N; i++) {
			for (int j = 1; j < M; j++) {
				dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]) + arr[i][j];
			}
		}

		System.out.println(dp[N - 1][M - 1]);
	}

}
