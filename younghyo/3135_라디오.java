
// 라디오(백준)
// 단순 구현

import java.util.StringTokenizer;
import java.io.*;

public class Main {


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer s = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(s.nextToken()); // 현재 주파수
        int B = Integer.parseInt(s.nextToken()); // 가고 싶은 주파수
        int N = Integer.parseInt(br.readLine()); // 즐겨찾기 수

        int min = Math.abs(A - B); // 최소값


        for(int i = 0; i < N; i++) {

            int likes = Integer.parseInt(br.readLine());

            min = Math.min(Math.abs(B - likes) + 1, min);
        }

        System.out.println(min);
    }
}
