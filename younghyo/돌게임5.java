// 백준 9659번: 돌 게임 5
// ...

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n + 1 + 1];
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 0;
        for (int i = 3; i <= n; i++) {
            int cy = i - 1;
            dp[i] = dp[cy - 1];
        }
        System.out.println(dp[n] == 0 ? "SK" : "CY");
        br.close();
    }
}
