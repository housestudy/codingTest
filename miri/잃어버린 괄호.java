import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = Integer.MAX_VALUE;

        StringTokenizer st = new StringTokenizer(br.readLine(), "-");

        while(st.hasMoreTokens()) {
            int answer = 0;

            StringTokenizer add = new StringTokenizer(st.nextToken(), "+");

            while(add.hasMoreTokens()) {
                answer += Integer.parseInt(add.nextToken());
            }

            if(sum == Integer.MAX_VALUE) {
                sum = answer;
            } else {
                sum -= answer;
            }
        }
        System.out.println(sum);
    }
}