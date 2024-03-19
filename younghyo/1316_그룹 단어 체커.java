// https://www.acmicpc.net/problem/1316
// 그룹단어 체커

import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int count = N;
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            boolean[] bArr = new boolean[26];
            for (int j = 0; j < str.length() - 1; j++) {
                if (str.charAt(j) != str.charAt(j + 1)) {
                    if (bArr[str.charAt(j + 1) - 'a']) {
                        count--;
                        break;
                    }
                }
                bArr[str.charAt(j) - 'a'] = true;
            }
        }
        System.out.println(count);
    }
}