package codingTest;
// 다리놓기 실패 ( 실버 5 ) , 백준 : https://www.acmicpc.net/problem/1010 
// DP , 조합 

import java.util.Scanner;

public class Solution0121 {

	public static void main(String[] args) {
			
		Scanner scn = new Scanner(System.in);
		
		int[][] dp = new int[30][30];
			
		for(int i = 0; i < 30; i++)
		{
			dp[i][i] = 1;
			dp[i][0] = 1;
		}
		
		for(int i = 2; i < 30; i++)
		{
			for(int j = 1; j < 30; j++)
			{
				dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
			}
		}
		
		int t = scn.nextInt();
		StringBuilder sb = new StringBuilder();
		
		for(int i = 0; i < t; i++)
		{
			int n = scn.nextInt();
			int m = scn.nextInt();
		
			sb.append(dp[m][n]).append("\n");
		}
		
		System.out.println(sb);
			
		
		
			
		
	}

}
