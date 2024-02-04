import java.io.*;
import java.util.*;

public class Main {
    StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n+1];
        List<Integer> result = new ArrayList<>();
        for(int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = n; i >0; i--) {
            result.add(arr[i],i);
        }
        for (Integer i : result) {
            System.out.print(i + " ");

        }

    }
}