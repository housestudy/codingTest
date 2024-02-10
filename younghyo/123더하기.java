// https://www.acmicpc.net/problem/9095 : 1 2 3 더하기
// DP , 점화식 재귀적으로 계산
import java.util.*;

public class Main {

	static int[] arr;
	
	public static void main(String[] args) {

		Scanner scn = new Scanner(System.in);
		
		arr = new int[11];
		
		arr[0] = 1;
		arr[1] = 1;
		arr[2] = 2;
		arr[3] = 4;
		// 초기값
		
		
		int n = scn.nextInt();
		
		
		for(int i = 0; i < n; i++) {
			int temp = scn.nextInt();
			System.out.println(cal(temp));
		}
	
		scn.close();
	}	
	
	public static int cal (int n) {
		if(arr[n] > 0) {
			return arr[n];
		}
		
		arr[n] = cal(n-1) + cal(n-2) + cal(n-3); //
		
		return arr[n];
		
	}
	
	
}