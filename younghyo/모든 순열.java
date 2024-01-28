// 백준문제 : 모든순열 (실버 3), https://www.acmicpc.net/problem/10974
// 백트래킹 보충
import java.util.*;

public class BackTrack {

	public static void main(String[] args) {

		Scanner scn = new Scanner(System.in);

		int N = scn.nextInt();
		int[] arr = new int[N]; 
		int[] output = new int[N];  
		boolean[] visited = new boolean[N]; 

		for (int i = 0; i < N; i++)
			arr[i] = i + 1;

		per(N, N, arr, output, visited, 0);
	}

	static void per(int N, int r, int[] arr, int[] output, boolean[] visited, int depth) {

		if (depth == r) {
			print(output, r);
			return;
		}

		for (int i = 0; i < N; i++) {
			if (visited[i] != true) {
				visited[i] = true; 
				output[depth] = arr[i]; 
				per(N, r, arr, output, visited, depth + 1); //
				visited[i] = false;
			}
		}

	}

	static void print(int[] arr, int r) {
	        for(int i=0; i<r; i++)
	            System.out.print(arr[i] + " ");
	        System.out.println();
	}

}
